import tkinter as tk
from tkinter import *
from tkinter import ttk

#settings
root = Tk()
root.title("App de prueba")
root.geometry("500x600")

menu = Menu(root)
optionstab = Menu(menu)
optionstab.add_command(label="Option 1")
optionstab.add_command(label="Option 2")
optionstab.add_command(label="exit")
menu.add_cascade(label="Options", menu=optionstab)
root.config(menu=menu)

def create_card():
    print("Apreté el botón :)")
    return

ttk.Label(text="FastFlashcards").pack()
ttk.Label(text="Add new card").pack()
card_entry = tk.StringVar()
ttk.Entry(textvariable=card_entry).pack(pady=5)
ttk.Button(text="Create Card", command=create_card).pack(pady=5)

root.mainloop()