"""
Пример создания меню и подменю с помощью виджета Menu
"""

from tkinter import Tk, Frame, Menu


class Example(Frame):
    """
    Клас приложения с наследованием от родительского класса Frame
    """

    def __init__(self, parent):
        """
        Конструктор класса приложения для создания главной рамки.
        :param parent: параметр для передачи ссылки на главное окно приложения
        """
        Frame.__init__(self, parent)  # вызов конструктора родительского класса виджета рамки
        self.parent = parent  # сохранение ссылки на главное окно приложения в параметрах объекта главной рамки
        self.init_ui()  # вызов метода построения интерфейса приложения

    def init_ui(self):
        """
        Метод построения интерфейса приложения
        """
        self.parent.title("Добавляем подменю")
        # задаем имя окна приложения через ссылку в параметрах объекта главной рамки приложения
        menubar = Menu(self.parent)  # создание панели меню для размещения в главном окне приложения
        self.parent.config(menu=menubar)  # настраиваем панель меню для отображения в качестве меню главного окна
        file_menu = Menu(menubar, tearoff=False)  # создание пункта меню панели меню для секции Файл в виде выпадающего
        submenu = Menu(file_menu, tearoff=False)  # создание подменю для секции меню Файл
        # списка команд. tearoff=False предотвращает отрыв выпадающего меню от панели. По умолчанию True
        menubar.add_cascade(label='Файл', underline=0, menu=file_menu)
        # привязка выпадающего меню к секции Файл и размещение секции Файл на панели меню
        file_menu.add_cascade(label='Импортировать', menu=submenu, underline=0)
        # добавление пункта меню в выпадающий список команд секции файл
        # underline=0 - подчеркивание 0-го символа в названии пункта меню
        file_menu.add_separator()  # добавление разделителя в выпадающий список команд
        file_menu.add_command(label='Выход', underline=0, command=self.on_exit)
        # добавление пункта выпадающего меню и привязка к нему вызова метода
        # underline=0 - подчеркивание 0-го символа в названии пункта меню
        submenu.add_command(label='Новый источник')  # добавление пункта в подменю в примере без вызова метода
        submenu.add_command(label='Закладки')
        submenu.add_command(label='Почта')

    def on_exit(self):
        """
        Метод выхода из приложения
        """
        self.quit()  # можно переместить непосредственно вместо вызова метода on_exit()


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