"""
Пример создания окна для выбора файла или папки с помощью filedialog
"""

from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog


class Example(Frame):
    """
    Класс приложения с наследованием от родительского класса виджета рамки
    """

    def __init__(self, parent: Tk) -> None:
        """
        Конструктор класса приложения.
        :param parent: параметр для передачи ссылки на главное окно приложения
        """
        Frame.__init__(self)  # вызов конструктора родительского класса виджета Frame
        self.parent = parent  # сохранение ссылки на главное окно в атрибуте приложения
        self.txt = Text(self)  # создание текстового поля для отображения содержимого выбранного файла
        self.init_ui()  # вызов метода инициализации графического интерфейса приложения

    def init_ui(self) -> None:
        self.parent.title('Окно для выбора файла')
        self.pack(fill=BOTH, expand=1)  # размещение главной рамки в главном окне с заполнением
        # по горизонтали и вертикали с установкой разрешения на растяжение
        # Если не поставить fill=BOTH, то текстовое не будет растягиваться более некоторого размера по умолчанию
        # Если не поставить expand=1, то текстовое поле будет растягиваться только по горизонтали
        menubar = Menu(self.parent)  # создание панели меню главного окна приложения
        self.parent.config(menu=menubar)  # настраиваем панель меню для отображения в качестве меню главного окна
        file_menu = Menu(menubar, tearoff=0)  # создаем объект меню в виде выпадающего списка команд
        # tearoff=0 предотвращает отрыв выпадающего меню от панели. по умолчанию True
        menubar.add_cascade(label='Файл', menu=file_menu)  # создание пункта Файл панели меню главного окна
        file_menu.add_command(label='Открыть', command=self.on_open)  # создание пункта меню Открыть в выпадающем меню
        # Файл с привязкой метода открытия диалогового окна для выбора файлов и папок
        self.txt.pack(fill=BOTH, expand=1)  # размещение текстового поля в главной рамке с заполнением
        # по горизонтали и вертикали с установкой разрешения на растяжение
        # Если не поставить fill=BOTH, то текстовое не будет растягиваться более некоторого размера по умолчанию
        # Если не поставить expand=1, то текстовое поле будет растягиваться только по горизонтали

    def on_open(self) -> None:
        """
        Метод открытия диалогового окна выбора файлов и папок
        """
        ftypes = [('Python файлы', '*.py'), ('Все файлы', '*')]  # создание правил фильтрации файлов
        dlg = filedialog.Open(self, filetypes=ftypes)  # создание и отображение диалогового окна выбора файлов и папок
        # с прикреплением правил фильтрации файлов
        fl = dlg.show()  # извлечение и сохранение в переменную пути выбранного файла в виде строки
        if fl != '':  # если переменная пути не пустая
            text = self.read_file(fl)  # вызывается метод чтения выбранного файла
            self.txt.insert(END, text)  # вставка возвращенного методом чтения файла текста в текстовое поле в конец

    @staticmethod
    def read_file(filename: str) -> str:
        """
        Метод чтения файла и сохранения его содержимого в текстовую переменную.
        :param filename: принимает путь к выбранному файлу.
        :return: возвращает прочитанное содержимое файла в виде строки
        """
        with open(filename, 'r', encoding='Utf-8') as f:  # открытие файла на чтение с помощью менеджера контекстов whit
            text = f.read()  # чтение всего содержимого файла с помощью метода read и запись полученной
            # строки в переменную
        return text  # возврат переменной со строкой


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения
    """
    root = Tk()  # создание главного окна приложения
    app = Example(root)  # создание объекта приложения с передачей ссылки на главное окно
    root.geometry('300x250+300+300')  # установка размеров и размещение главного окна приложения по координатам
    # NW угла
    root.mainloop()  # запуск главного цикла приложения


if __name__ == '__main__':  # данное условие предотвращает запуск кода верхнего уровня модуля при его импортировании
    main()  # вызов функции запуска кода верхнего уровня
