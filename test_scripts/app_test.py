import tkinter as tk
from tkinter import *
from tkinter import ttk
import settings



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("FastFlashcards v0.1")
        self.root.geometry("500x600")
        
        self.create_menu()
        self.create_widgets()
        
    def create_menu(self):
        #Adds menu bar on top of app
        menu = Menu(self.root)
        options_tab = Menu(menu)
        options_tab.add_command(label="Option 1")
        options_tab.add_command(label="Option 2")
        options_tab.add_command(label="exit", command=self.root.destroy)
        menu.add_cascade(label="Options", menu=options_tab)
        self.root.config(menu=menu)
    
    def create_widgets(self):
        #Adds widgets
        self.title = tk.Label(self.root, text="FastFlashcards", font=("arial",30)).pack(pady=25)
        
        self.kl_frame = tk.Frame(self.root)
        self.kl = tk.StringVar()
        tk.Label(self.kl_frame, text="Known Language: ").pack(side=tk.LEFT)
        tk.Entry(self.kl_frame, textvariable=self.kl).pack(side=tk.LEFT)
        self.kl_frame.pack()
        self.tl_frame = tk.Frame(self.root)
        self.tl = StringVar()
        tk.Label(self.tl_frame, text="Target Language: ").pack(side=tk.LEFT)
        tk.Entry(self.tl_frame, textvariable=self.tl).pack(side=tk.LEFT)
        self.tl_frame.pack()
        
        tk.Label(self.root, text="Enter text to make card!").pack(pady=5)
        self.entry_frame = tk.Frame(self.root)
        self.card_entry = tk.StringVar()
        ttk.Entry(self.entry_frame, textvariable=self.card_entry).pack(side=tk.LEFT, padx=5)
        self.cards_added = 0
        self.added_cards_strvar = tk.StringVar()
        self.added_cards_strvar.set("")
        tk.Button(self.entry_frame, text="Create Card", command=self.make_card).pack()
        self.entry_frame.pack()
        tk.Label(self.root, textvariable=self.added_cards_strvar).pack()
        
    def make_card(self):
        #Makes card?
        self.cards_added += 1
        self.added_cards_strvar.set(f"Added {self.cards_added} cards to deck.")
        
    

root = tk.Tk()
app = App(root)
root.mainloop()