"""
Пример создания команд вызова функций/методов для виджетов кнопки
Запись текста в Label и чтение из него по индексу ['text']
"""
import tkinter as tk


def increase():  # функции размещаются до основного цикла окна
    value = int(lbl_value['text'])  # у label нет метода get, текст считывается как из словаря по индексу 'text'
    lbl_value['text'] = f'{value + 1}'  # записывается текст в label, также как и читается, по индексу 'text'


def decrease():
    value = int(lbl_value['text'])
    lbl_value['text'] = f'{value - 1}'


window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text='-', command=decrease)  # параметр command связывает кнопку с функцией
btn_decrease.grid(row=0, column=0, sticky='nsew')

lbl_value = tk.Label(master=window, text='0')
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text='+', command=increase)
btn_increase.grid(row=0, column=2, sticky='nsew')

window.mainloop()
