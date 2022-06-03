"""
Пример применения менеджера геометрии pack
"""
import tkinter as tk
import tkinter.ttk as ttk


class Example(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)  # вызов конструктора родительского класса
        self.parent = parent  # сохранение ссылки на основное окно
        self.init_ui()  # инициализация интерфейса

    def init_ui(self):
        self.parent.title('Оставить отзыв')  # установка имени окна
        self.pack(fill=tk.BOTH, expand=True)  # размещение базовой рамки, в которой будут размещаться остальные рамки
        frame1 = ttk.Frame(self)  # создание рамки для размещения надписи и однострочного поля ввода
        frame1.pack(fill=tk.X)  # размещение рамки с заполнением по горизонтали
        lbl1 = ttk.Label(frame1, text='Заголовок', width=10)  # создание надписи для названия поля ввода
        lbl1.pack(side=tk.LEFT, padx=5, pady=5)  # размещение надписи с отступами 5 пикселей и выравниванием слева
        entry1 = ttk.Entry(frame1)  # создание однострочного поля ввода
        entry1.pack(fill=tk.X, padx=5, expand=True)  # размещение однострочного поля ввода с заполнением по горизонтали
        frame2 = ttk.Frame(self)  # создание рамки для размещения надписи и однострочного поля ввода
        frame2.pack(fill=tk.X)  # размещение рамки с заполнением по горизонтали
        lbl2 = ttk.Label(frame2, text='Автор', width=10)  # создание надписи для названия поля ввода
        lbl2.pack(side=tk.LEFT, padx=5, pady=5)  # размещение надписи с отступами 5 пикселей и выравниванием слева
        entry2 = ttk.Entry(frame2)  # создание однострочного поля ввода
        entry2.pack(fill=tk.X, padx=5, expand=True)  # размещение однострочного поля ввода с заполнением по горизонтали
        frame3 = ttk.Frame(self)  # создание рамки для размещения надписи и однострочного поля ввода
        frame3.pack(fill=tk.BOTH, expand=True)  # размещение рамки с заполнением по горизонтали и вертикали
        lbl3 = ttk.Label(frame3, text='Отзыв', width=10)  # создание надписи для названия поля ввода
        lbl3.pack(side=tk.LEFT, anchor=tk.N, padx=5, pady=5)  # размещение надписи с отступами 5 пикселей и выравниванием слева
        txt = tk.Text(frame3)  # создание многострочного текстового поля ввода
        txt.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)  # размещение многострочного текстового поля ввода


def main():
    root = tk.Tk()
    root.geometry('300x300+300+300')
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
