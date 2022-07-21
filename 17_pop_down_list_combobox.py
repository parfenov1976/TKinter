"""
Пример создания выпадающего списка
"""

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title('Выпадающий список')
root.geometry('400x250')
combo = ttk.Combobox(root)
combo['values'] = (1, 2, 3, 4, 5, 'Текст')
combo.current(5)
combo.pack(anchor=tk.NW)
combo.bind()
# TODO разобраться с получением выбранного из виджета
tk.Label(root, text='select').pack(padx=100, pady=100)
root.mainloop()
