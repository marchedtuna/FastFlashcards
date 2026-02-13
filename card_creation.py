import os, shutil
from googletrans import Translator
from bs4 import BeautifulSoup
import requests
from gtts import gTTS
import asyncio

from settings import Settings

settings = Settings()

async def translate_text(text, settings):
     async with Translator() as translator:
        textdict = {}
        language = await translator.detect(text)
        if language.confidence < 0.1 or language.lang not in [settings.known_lang, settings.target_lang]:
                print(f"WARNING: Couldn't detect language at {text}! Assuming text is in {settings.known_lang}.")
                translated = await translator.translate(text, src=settings.known_lang, dest=settings.target_lang)
                textdict["text_known_lang"] = text
                textdict["text_target_lang"] = translated.text
                return textdict
        elif language.lang == settings.known_lang:
                translated = await translator.translate(text, src=settings.known_lang, dest=settings.target_lang)
                textdict["text_known_lang"] = text
                textdict["text_target_lang"] = translated.text
                return textdict
        elif language.lang == settings.target_lang:
                translated = await translator.translate(text, src=settings.target_lang, dest=settings.known_lang)
                textdict["text_known_lang"] = translated.text
                textdict["text_target_lang"] = text
                return textdict
        else:
                print(f"Error when translating {text}")
                return -1
        
def download_image(word, settings):
        url = f'https://www.google.com/search?q={word}&source=lnms&tbm=isch&tbs=isz:m'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        imgs = soup.find_all("img")
        img_urls = [img["src"] for img in imgs if "src" in img.attrs]

        for img_url in img_urls[1:4]:
                try:
                        img_response = requests.get(img_url)
                        media_path = os.path.join(os.getenv("APPDATA"),"Anki2", "User 1", "collection.media")
                        img_path = os.path.join(media_path, f"{settings.standard_deck_name}-{word}.jpg")
                        with open(img_path, "wb") as f:
                                f.write(img_response.content)
                        return f'<img src="{settings.standard_deck_name}-{word}.jpg">'
                except Exception as e:
                        print(f"Error downloading image: {e}")
        return -1

def download_audio(word, lang, settings):
        speech = gTTS(word, lang=lang)
        speech.save(f"{settings.standard_deck_name}-{word}-{lang}.mp3")
        source_path = os.path.join(os.getcwd(), f"{settings.standard_deck_name}-{word}-{lang}.mp3")
        media_path = os.path.join(os.getenv("APPDATA"),"Anki2", "User 1", "collection.media")
        destination_path = os.path.join(media_path, f"{settings.standard_deck_name}-{word}-{lang}.mp3")
        
        shutil.move(source_path, destination_path)
        return f'[sound:{settings.standard_deck_name}-{word}-{lang}.mp3]'

async def async_fill_details(text, settings):
        full_query = settings.front_format + ";" + settings.back_format
        
        textdict = await translate_text(text, settings)
        card_details = textdict
        card_details["id"] = len(settings.card_list)+1
        
        if "[AKL]" in full_query:
                card_details["audio_known_lang"] = download_audio(textdict[settings.known_lang], settings.known_lang, settings)
        else:
                card_details["audio_known_lang"] = ""
        if "[ATL]" in full_query:
                card_details["audio_target_lang"] = download_audio(textdict[settings.target_lang], settings.target_lang, settings)
        else:
                card_details["audio_target_lang"] = ""
        if "[IMG]" in full_query:
                card_details["image"] = download_image(text)
        else:
                card_details["image"] = ""
        settings.card_list.append(card_details)
        return card_details
    
def fill_details(text, settings):
    asyncio.run(async_fill_details(text, settings))

def add_line(card_details, settings):
        map = {
                "[TKL]":card_details["text_known_lang"],
                "[TTL]":card_details["text_target_lang"],
                "[AKL]":card_details["audio_known_lang"],
                "[ATL]":card_details["audio_target_lang"],
                "[IMG]":card_details["image"],
                "\n":"<br>"
        }
        
        front_format = settings.front_format
        back_format = settings.back_format
        for decorator in map:
                front_format = front_format.replace(decorator, map[decorator])
                back_format = back_format.replace(decorator, map[decorator])
        return f'{settings.standard_deck_name}	{front_format}	{back_format}\n'