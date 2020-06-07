import json
from difflib import get_close_matches
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

win = ThemedTk(theme="radiance")
win.title('English Dictionary')

data = json.load(open("Vocab.json"))

def translate():
    w = word.get()
    print(w)
    w = w.lower()
    if w in data:
        if type(data[w]) == list:
            for item in data[w]:
                showinfo("Result", f"{item}")
        else:
            showinfo("Result", f"{data[w]}")
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = messagebox.askquestion("Confirm",f"Did you mean instead? {get_close_matches(w, data.keys())[0]}")
        if yn=='yes':
            k = data[get_close_matches(w, data.keys())[0]]
            if type(k) == list:
                for item in k:
                    showinfo("Result", f"{item}")
            else:
                showinfo("Result", f"{data[get_close_matches(w, data.keys())[0]]}")
        elif yn=='no':
            msg = "We didn't understand your entry."
            showerror("Error", f"{msg}")
    else:
        msg = "The word doesn't exist. Please double check it."
        showerror("Error",f"{msg}")

label = tk.Label(win, text="Enter word: ")
label.grid(row=0,column=0,padx=8,pady=8)
word = tk.Entry(win)
word.grid(row=0,column=1,padx=8)

button =ttk.Button(win,text="Search",command=translate)
button.grid(row=1,column=0,columnspan=2,padx=8)

win.mainloop()
