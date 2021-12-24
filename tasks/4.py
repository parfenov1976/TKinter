import tkinter as tk
from random import randint


def roll():
    lbl_dice['text'] = randint(1, 6)


window = tk.Tk()

window.rowconfigure([0, 1], minsize=50)
window.columnconfigure(0, minsize=150)

btn_roll = tk.Button(text='Бросить кость', command=roll)
btn_roll.grid(row=0, column=0, sticky='nsew')

lbl_dice = tk.Label()
lbl_dice.grid(row=1, column=0)

window.mainloop()
