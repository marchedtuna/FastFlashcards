import tkinter as tk
from tkinter import *

from settings import Settings
from app import App

settings = Settings()
root = tk.Tk()
app = App(root, settings)
app.root.mainloop()