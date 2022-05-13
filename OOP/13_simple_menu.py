"""
Пример создания простого меню
"""

from tkinter import Tk, Frame, Menu


class Example(Frame):
    """
    Создание объекта главной рамки приложения - экземпляра класса виджета рамки
    """

    def __init__(self, parent):
        """
        Конструктор приложения.
        :param parent: ссылка на основное окно
        """
        Frame.__init__(self, parent)  # вызов конструктора родительского класса
        self.parent = parent  # сохранение ссылки на главное окно приложения в атрибуте главной рамки
        self.init_ui()  # вызов метода для создания интерфейса приложения

    def init_ui(self):
        """
        Метод, создающий графический пользовательский интерфейс приложения
        """
        self.parent.title('Простое меню')  # присвоение названия окну приложения через ссылку на него
        menubar = Menu(self.parent)  # создание объекта панели меню главного окна
        self.parent.config(menu=menubar)  # настраиваем панель меню для отображения в качестве меню главного окна
        file_menu = Menu(menubar, tearoff=False)  # создаем объект меню в виде выпадающего списка команд
        # tearoff=False предотвращает отрыв выпадающего меню от панели. по умолчанию True
        file_menu.add_command(label='Выход', command=self.on_exit)
        # добавление пункта выпадающего меню и привязка к нему вызова метода
        file_menu.add_command(label='Пусто')
        menubar.add_cascade(label='Файл', menu=file_menu)
        # привязка выпадающего меню к секции Файл и размещение секции Файл на панели меню

    def on_exit(self):
        """
        Метод для закрытия главного окна приложения
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
