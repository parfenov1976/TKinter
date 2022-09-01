"""
Пример использования круглых переключателей (radio buttons)
"""
import tkinter as tk
import tkinter.ttk as ttk


def clicked():
    print('===')


window = tk.Tk()
window.title('Круглые переключатели радиокнопки')
window.geometry('400x250')
rad1 = ttk.Radiobutton(window, text='Первый', value=1, command=clicked)
rad2 = ttk.Radiobutton(window, text='Второй', value=2)
rad3 = ttk.Radiobutton(window, text='Третий', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
rad4 = ttk.Radiobutton(window, text='Четвертый', value=4, command=clicked)
rad5 = ttk.Radiobutton(window, text='Пятый', value=5)
rad6 = ttk.Radiobutton(window, text='Шестой', value=6)
rad4.grid(column=0, row=1)
rad5.grid(column=1, row=1)
rad6.grid(column=2, row=1)
window.mainloop()
