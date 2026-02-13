import tkinter as tk
from tkinter import *
from tkinter import ttk
import json

class Settings:
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        self.card_list = []
        self.known_lang = "en"
        self.target_lang = "es"
        self.front_format = "[TKL]"
        self.back_format = "[TTL]"
        self.deck_name = "Unnamed Deck"
        
    def reset(self):
        settings_json = {
            "known_lang": "en",
            "target_lang": "es",
            "front_format": "[TKL]",
            "back_format": "[TTL]",
            "deck_name": "Unnamed Deck"
        }
        with open("settings.json","w") as file:
            json.dump(settings_json, file)
        self.get()
        self.window.destroy()
        
    def get(self):
        self.KnownLang = tk.StringVar()
        self.TargetLang = tk.StringVar()
        self.FrontFormat = tk.StringVar()
        self.BackFormat = tk.StringVar()
        self.DeckName = tk.StringVar()
        
        with open("settings.json", "r") as f:
            settings_json = json.load(f)
            self.known_lang = settings_json["known_lang"]
            self.target_lang = settings_json["target_lang"]
            self.front_format = settings_json["front_format"]
            self.back_format = settings_json["back_format"]
            self.deck_name = settings_json["deck_name"]
        
        self.card_list = []
        self.KnownLang.set(self.known_lang)
        self.TargetLang.set(self.target_lang)
        self.FrontFormat.set(self.front_format)
        self.BackFormat.set(self.back_format)
        self.DeckName.set(self.deck_name)
    
    def set(self):
        self.known_lang = self.KnownLang.get()
        self.target_lang = self.TargetLang.get()
        self.front_format = self.FrontFormat.get()
        self.back_format = self.BackFormat.get()
        self.deck_name = self.DeckName.get()
        self.standard_deck_name = self.deck_name.lower().replace(" ","_")
        
        settings_json = {
            "known_lang": self.known_lang,
            "target_lang": self.target_lang,
            "front_format": self.front_format,
            "back_format": self.back_format,
            "deck_name": self.deck_name
        }
        with open("settings.json","w") as file:
            json.dump(settings_json, file)
    
    def open(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("FastFlashcards v0.1.0 - Settings")
        self.window.geometry("300x250")
        
        self.make_widgets()
        self.window.grab_set()
    
    def make_widgets(self):
        tk.Label(self.window, text="Settings").pack(pady=10)
        
        self.get()
        print(f"KnownLang = {self.KnownLang.get()}, TargetLang = {self.TargetLang.get()}")
        
        deck_name_frame = tk.Frame(self.window)
        tk.Label(deck_name_frame, text="Deck Name:").pack(side=tk.LEFT, padx=1)
        tk.Entry(deck_name_frame, textvariable=self.DeckName).pack(padx=5)
        deck_name_frame.pack(anchor="w", pady=3)
        
        known_lang_frame = tk.Frame(self.window)
        tk.Label(known_lang_frame, text="Known Language:").pack(side=tk.LEFT, padx=1)
        tk.Entry(known_lang_frame, textvariable=self.KnownLang).pack(padx=5)
        known_lang_frame.pack(anchor="w", pady=3)
        
        target_lang_frame = tk.Frame(self.window)
        tk.Label(target_lang_frame, text="Target Language:").pack(side=tk.LEFT, padx=1)
        tk.Entry(target_lang_frame, textvariable=self.TargetLang).pack(padx=5)
        target_lang_frame.pack(anchor="w", pady=3)
        
        front_format_frame = tk.Frame(self.window)
        tk.Label(front_format_frame, text="Front Format:").pack(side=tk.LEFT, padx=1)
        tk.Entry(front_format_frame, textvariable=self.FrontFormat).pack(padx=5)
        front_format_frame.pack(anchor="w", pady=3)
        
        back_format_frame = tk.Frame(self.window)
        tk.Label(back_format_frame, text="Back Format:").pack(side=tk.LEFT, padx=1)
        tk.Entry(back_format_frame, textvariable=self.BackFormat).pack(padx=5)
        back_format_frame.pack(anchor="w", pady=3)
        
        buttons_frame = tk.Frame(self.window)
        tk.Button(buttons_frame, text="Confirm", command=self.set).pack(side=tk.LEFT, padx=5)
        tk.Button(buttons_frame, text="Reset All", command=self.reset).pack(padx=5)
        buttons_frame.pack(pady=10)
        
#settings = Settings()
#settings.open()