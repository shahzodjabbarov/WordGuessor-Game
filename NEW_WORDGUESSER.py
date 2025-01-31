from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox
from openpyxl import Workbook, load_workbook

import time
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)





window = Tk()

window.geometry("700x550")
window.configure(bg = "#140149")

filename=PhotoImage(file=relative_to_assets(("pic2.png")))
background_label=Label(window,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

word_list = ['apple', 'school', 'book', 'pencil', 'phone', 'tiktok', 'laptop', 'internet', 'banana']

word = ''
key_word = ''
letters = []
hidden_letters = []
counter = 0


def starter():
    global word
    global key_word
    global letters
    global hidden_letters
    global counter
    word = ''
    key_word = ''
    letters = []
    hidden_letters = []
    counter = 0

    key_word = word_list[random.randint(0, len(word_list) - 1)]
    word = "x" * len(key_word)

    entry_1.configure(text=word)

    for i in key_word:
        letters.append(i)
    for i in word:
        hidden_letters.append(i)



    

def enter():
    global word
    global key_word
    global letters
    global hidden_letters
    global counter
    

   
    ask = entry_2.get().lower()
    entry_2.delete(0, tk.END)
    counter = counter + 1

    for i in letters:
        if ask == i:
            hidden_letters[letters.index(i)] = ask
            letters[letters.index(i)] = "0"
            word = ''
            word = word.join(hidden_letters)
            
    entry_1.configure(text=word)

    
    if word == key_word:
        entry_1.configure(text="YOU WON")
    
    if counter > (len(key_word) + 3):
        entry_1.configure(text='YOU LOST')
       

def exit():
    window.destroy()




entry_1 = Label(text=word, font = ("Didot", 16), 
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=232.0,
    y=97.0,
    width=237.0,
    height=43.0
)


entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=304.0,
    y=319.0,
    width=92.0,
    height=32.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: enter(),
    relief="flat"
)
button_1.place(
    x=273.0,
    y=375.0,
    width=154.0,
    height=45.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: starter(),
    relief="flat"
)
button_2.place(
    x=17.5,
    y=488.0,
    width=98.0,
    height=45.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: exit(),
    relief="flat"
)
button_3.place(
    x=582.0,
    y=488.0,
    width=98.0,
    height=45.0
)
window.resizable(False, False)
window.mainloop()
