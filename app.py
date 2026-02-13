import tkinter as tk
import os
from tkinter import *
from tkinter import ttk

from settings import Settings
from card_creation import fill_details, add_line

settings = Settings()

class App:
    def __init__(self, root, settings):
        self.root = root
        self.root.title("FastFlashcards v0.1.0")
        self.root.geometry("300x500")
        
        self.make_widgets()
    
    def make_widgets(self):
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
        tk.Button(self.entry_frame, text="Create Card", command=self.upload_text).pack()
        self.entry_frame.pack()
        tk.Label(self.root, textvariable=self.AddedCards).pack()
        tk.Button(self.root, text="Export TXT File", command=self.make_txt).pack(pady=15)
        
    def upload_text(self):
        #Makes card?
        text = self.card_text.get()
        if text == "":
            return
        card_details = fill_details(text, settings)
        
        self.card_text.set("")
        self.cards_added += 1
        self.AddedCards.set(f"Added {self.cards_added} cards to deck.")
        print(f"kl: {settings.known_lang}, tl: {settings.target_lang}")
        return card_details
    
    def make_txt(self):
        initial_dir = os.getcwd()
        os.chdir(os.path.join(initial_dir, "decks"))
        txt_path = os.path.join(os.getcwd(), f"{settings.standard_deck_name}.txt")
        
        if not os.path.isfile(txt_path):
            with open(f"{settings.standard_deck_name}.txt", "w") as txt:
                txt.write("#separator:tab\n")
                txt.write("#html:true\n")
                txt.write("#deck column: 1\n")
                txt.write("#tags column: 4\n")
                txt.close()
        
        txt = open(f"{settings.standard_deck_name}.txt", "a")
        print(".txt file opened")
        for card_details in settings.card_list:
            txt.write(add_line(card_details, settings))
        txt.close()
        os.chdir("..")