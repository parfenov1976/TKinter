"""
Пример размещения изображения на холсте
"""

import tkinter as tk
import PIL.Image
import PIL.ImageTk


class Example(tk.Frame):
    """
    Подкласс приложения с наследованием от родительского класса Frame
    """
    def __init__(self, parent: tk) -> None:
        """
        Конструктор класса приложения
        :param parent: параметр для передачи ссылки на главное окно приложения
        """
        tk.Frame.__init__(self)  # вызов конструктора родительского класса
        self.parent = parent  # сохранение ссылка на главное окно приложения в параметрах экземпляра приложения
        self.img = PIL.Image.open('tatras.jpg')  # создание объекта изображения из файла
        self.tatras = PIL.ImageTk.PhotoImage(self.img)  # создание фотоизображения из объекта изображения
        self.init_ui()  # вызов метода инициализации графического интерфейса

    def init_ui(self) -> None:
        """
        Метод инициализации графического интерфейса
        """
        self.parent.title('Изображение в Canvas')
        self.pack(fill=tk.BOTH, expand=1)  # размещение главной рамки в главном окне с заполнением
        # по горизонтали и вертикали с установкой разрешения на растяжение
        # Если не поставить fill=BOTH, то холст не будет растягиваться более некоторого размера по умолчанию
        # Если не поставить expand=1, то холст будет растягиваться только по горизонтали
        canvas = tk.Canvas(                     # создание холста
            self, width=self.img.size[0]+20,    # ширина на 20 больше ширины изображения
            height=self.img.size[1] + 20        # высота на 20 больше высоты изображения
        )
        canvas.create_image(10, 10, anchor=tk.NW, image=self.tatras)  # размещение изображения на холсте с привязкой
        # ВЛ угла
        canvas.pack(fill=tk.BOTH, expand=1)  # размещение холста в главной рамке с заполнением
        # по горизонтали и вертикали с установкой разрешения на растяжение
        # Если не поставить fill=BOTH, то холст не будет растягиваться более некоторого размера по умолчанию
        # Если не поставить expand=1, то холст будет растягиваться только по горизонтали


def main() -> None:
    """
    Функция с кодом приложения верхнего уровня
    """
    root = tk.Tk()  # создание главного окна приложения
    app = Example(root)  # создание объекта приложения с передачей ссылки на главное окно приложения
    root.mainloop()  # запуск главного цикла приложения


if __name__ == '__main__':  # условия проверки для предотвращения запуска кода верхнего уровня при импортировании
    # данного файла как модуля
    main()  # вызов функции с кодом верхнего уровня
