"""
Пример расположение картинок в главной рамке по абсолютным координатам помощью менеджера
геометрии place
"""
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.ttk as ttk


class Example(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)  # вызов конструктора родительского класса
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title('Absolute positioning')
        self.pack(fill=tk.BOTH, expand=1)
        ttk.Style().configure("TFrame", background="#333")  # изменение цвета фона виджета при помощи стиля
        bard = Image.open('bardejov.jpg')  # создание объекта изображения
        bardejov = ImageTk.PhotoImage(bard)  # создание объекта фотоизображения из объекта изображения
        label1 = ttk.Label(self, image=bardejov)  # создание ярлыка с изображением
        label1.image = bardejov  # сохраняем ссылку на изображение
        label1.place(x=20, y=20)  # размещение ярлыка по координатам
        rot = Image.open('rotunda.jpg')  # создание объекта изображения
        rotunda = ImageTk.PhotoImage(rot)  # создание объекта фотоизображения из объекта изображения
        label2 = ttk.Label(self, image=rotunda)  # создание ярлыка с изображением
        label2.image = rotunda  # сохраняем ссылку на изображение
        label2.place(x=40, y=160)  # размещение ярлыка по координатам
        minc = Image.open('mincol.jpg')  # создание объекта изображения
        mincol = ImageTk.PhotoImage(minc)  # создание объекта фотоизображения из объекта изображения
        label3 = ttk.Label(self, image=mincol)  # создание ярлыка с изображением
        label3.image = mincol  # сохраняем ссылку на изображение
        label3.place(x=170, y=50)  # размещение ярлыка по координатам


def main():
    root = tk.Tk()
    root.geometry('300x280+300+300')
    Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
