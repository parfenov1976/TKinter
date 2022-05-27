"""
Пример созданию всплывающего меню (по аналогии с контекстным меню по ПКМ)
"""

from tkinter import Tk, Frame, Menu


class Example(Frame):
    """
    Класс приложения с наследованием от родительского класс Frame
    """

    def __init__(self, parent):
        """
        Конструктор класса приложения для создания главной рамки и объектов интерфейса.
        :param parent: параметр для передачи ссылки на главное окно приложения
        """
        Frame.__init__(self, parent)  # вызов конструктора родительского класса Frame
        self.parent = parent  # сохранение ссылки на главное окно приложения в атрибут объекта приложения
        self.menu = Menu(self.parent, tearoff=0)  # создание меню и сохранение его в атрибут приложения
        # tearoff=0 предотвращает отрыв всплывающего меню от окна приложения. По умолчанию True(1)
        self.init_ui()  # вызов метода сборки графического интерфейса приложения

    def init_ui(self):
        """
        Метода для сборки интерфейса приложения
        """
        self.parent.title('Всплывающее меню')  # присвоение имени главного окна через атрибут объекта приложения
        self.pack()  # размещение главной рамки в главном окне приложения
        self.menu.add_command(label='Бип!', command=self.bell)  # добавление пункта во всплывающее меню и связывание
        # его с командой вызова метода bell() для воспроизведения системного звука колокольчик
        self.menu.add_command(label='Выход', command=self.on_exit)  # добавление пункта во всплывающее меню и связывание
        # его с методом, вызывающем команду на закрытие приложения
        self.parent.bind('<Button-3>', self.show_menu)  # назначение события клика ПКМ привязка к нему метода,
        # дающего команду на вывод меню

    def show_menu(self, cur_coord):
        """
        Метод, дающий команду на вывод всплывающего меню
        :param cur_coord: передача координат курсора мыши
        """
        self.menu.post(cur_coord.x_root, cur_coord.y_root)  # команда для размещения меню по координатам

    def on_exit(self):
        """
        Метод, подающий команду на закрытие приложения
        """
        self.quit()


def main():
    """
    Функция запуска кода верхнего уровня приложения
    """
    root = Tk()  # создание главного окна приложения
    root.geometry('250x150+300+300')  # установка размера главного окна и его размещение
    app = Example(root)  # создание экземпляра приложения с передачей ссылки на главное окно
    root.mainloop()  # запуск основного цикла главного окна приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуск main при импортировании данного файла как модуля
    main()