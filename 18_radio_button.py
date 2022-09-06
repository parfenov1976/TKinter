"""
Пример использования круглых переключателей (radio buttons)
"""
import tkinter as tk
import tkinter.ttk as ttk


def clicked_1() -> None:
    """
    Метод клика для 1-ой группы радио кнопок.
    """
    lbl1['text'] = group_1.get()  # изменение содержимого ярлыка 1-ой группы радио кнопок


def clicked_2() -> None:
    """
    Метод клика для 2-ой группы радио кнопок.
    """
    lbl2['text'] = group_2.get()  # изменение содержимого ярлыка 1-ой группы радио кнопок


window = tk.Tk()  # создание главного окна приложения
window.title('Круглые переключатели радиокнопки')  # присвоение названия главному окну приложения
window.geometry('400x250')  # установление размеров главного окна приложения
group_1 = tk.IntVar()  # создание хранилища значений для 1-й группы радио кнопок
group_2 = tk.IntVar()  # создание хранилища значений для 2-й группы радио кнопок
rad1 = ttk.Radiobutton(window, text='Первый', variable=group_1, value=1, command=clicked_1)
# создание радио кнопки 1, присвоение ей имени и значения, хранилища значения и связывание с методом клика
rad2 = ttk.Radiobutton(window, text='Второй', variable=group_1, value=2, command=clicked_1)
rad3 = ttk.Radiobutton(window, text='Третий', variable=group_1, value=3, command=clicked_1)
rad1.grid(column=0, row=0)  # размещение кнопки в сетке
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
lbl1 = tk.Label(text='---')  # создание ярлыка для 1-ой группы радио кнопок
lbl1.grid(column=3, row=0)   # размещение ярлыка в сетке
rad4 = ttk.Radiobutton(window, text='Четвертый', variable=group_2, value=4, command=clicked_2)
rad5 = ttk.Radiobutton(window, text='Пятый', variable=group_2, value=5, command=clicked_2)
rad6 = ttk.Radiobutton(window, text='Шестой', variable=group_2, value=6, command=clicked_2)
rad4.grid(column=0, row=1)
rad5.grid(column=1, row=1)
rad6.grid(column=2, row=1)
lbl2 = tk.Label(text='---')
lbl2.grid(column=3, row=1)
window.mainloop()  # запуск основного цикла главного окна приложения
