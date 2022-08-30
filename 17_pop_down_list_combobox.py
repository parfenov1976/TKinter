"""
Пример создания выпадающего списка
"""
import time
import tkinter as tk
import tkinter.ttk as ttk


def relabel(event):
    lbl['text'] = combo.get()


root = tk.Tk()
root.title('Выпадающий список')
root.geometry('400x250')
combo = ttk.Combobox(root)
combo['values'] = (1, 2, 3, 4, 5, 'Текст')
combo.current(5)
combo.pack(anchor=tk.NW)
lbl = tk.Label(root, text=combo.get())
lbl.pack(padx=100, pady=100)
combo.bind("<<ComboboxSelected>>", relabel)
root.mainloop()
