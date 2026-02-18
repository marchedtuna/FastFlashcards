import tkinter as tk
import os
from tkinter import *
from tkinter import ttk

from settings import Settings
from card_creation import stored_name, fill_details, add_line

global version
version = "0.1.1"

settings = Settings()

class App:
    def __init__(self, root, settings):
        self.root = root
        self.root.title(f"FastFlashcards v{version}")
        self.root.geometry("300x500")
        
        self.make_widgets(settings)
    
    def make_widgets(self, settings):
        #Adds widgets
        tk.Button(self.root, text="Settings", command=lambda: settings.open(self.root)).pack(anchor="e")
        tk.Label(self.root, text="FastFlashcards", font=("arial",30)).pack(pady=25)
        
        tk.Label(self.root, text="Enter text to make card!").pack(pady=5)
        self.entry_frame = tk.Frame(self.root)
        self.card_text = tk.StringVar()
        ttk.Entry(self.entry_frame, textvariable=self.card_text).pack(side=tk.LEFT, padx=5)
        self.cards_added = 0
        self.AddedCards = tk.StringVar()
        self.AddedCards.set("")
        tk.Button(self.entry_frame, text="Create Card", command=lambda: self.upload_text(settings)).pack()
        self.entry_frame.pack()
        tk.Label(self.root, textvariable=self.AddedCards).pack()
        tk.Button(self.root, text="Export TXT File", command=lambda: self.make_txt(settings)).pack(pady=15)
        #tk.Button(self.root, text="Print Settings", command=lambda: self.print_settings(settings)).pack(pady=15)
        
    def print_settings(self, settings):
        #For debugging
        print(f"known_lang: {settings.known_lang}")
        print(f"target_lang: {settings.target_lang}")
        print(f"front_format: {settings.front_format}")
        print(f"back_format: {settings.back_format}")
        print(f"deck_name: {settings.deck_name}")
        print(f"card_list: {settings.card_list}")
        
    def upload_text(self, settings):
        #Makes card?
        text = self.card_text.get()
        if text == "":
            return
        card_details = fill_details(text, settings)
        
        self.card_text.set("")
        self.cards_added += 1
        self.AddedCards.set(f"Added {self.cards_added} cards to deck.")
        return card_details
    
    def make_txt(self, settings):
        initial_dir = os.getcwd()
        os.chdir(os.path.join(initial_dir, "decks"))
        
        with open(f"{stored_name(settings.deck_name)}.txt", "w") as txt:
            txt.write("#separator:tab\n")
            txt.write("#html:true\n")
            txt.write("#deck column: 1\n")
            txt.write("#tags column: 4\n")
        
            print(".txt file opened")
            for card_details in settings.card_list:
                l = add_line(card_details, settings)
                print(f"Line: {l}")
                txt.write(l)
            txt.close()
        
        os.chdir("..")