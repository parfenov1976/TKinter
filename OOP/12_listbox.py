"""
Пример использования виджета Listbox
"""

from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter.ttk import Frame, Label


class Example(Frame):
    """
    Класс приложения от родительского класса виджета Frame
    """

    def __init__(self, parent):
        """
        Конструктор приложения.
        :param parent: ссылка на основное окно
        """
        Frame.__init__(self)  # вызов конструктора родительского класса для создания главной рамки
        self.parent = parent  # сохранение ссылки на основное окно
        self.var = StringVar()  # Создание переменной для хранения значения ярлыка (см. ниже)
        self.init_ui()  # вызов метода, создающего интерфейс

    def init_ui(self):
        """
        Метод, создающий графический пользовательский интерфейс приложения
        """
        self.parent.title('Список в Tkinter')  # присвоение имени главному окну через ссылку в аттрибутах главной рамки
        self.pack(fill=BOTH, expand=1)  # размещение главной рамки с помощью менеджера геометрии pack
        acts = ['Скарлет Йоханссон', 'Рейчел Вайс',  # создание списка
                'Натали Портман', 'Джессика Альба']
        lb = Listbox(self)  # создание экземпляра виджета Listbox
        for i in acts:  # помещение элементов списка в виджет listbox
            lb.insert(END, i)
        lb.bind('<<ListboxSelect>>', self.on_select)
        # назначение события, генерируемого при выборе элемента списка с закреплением к нему вызова метода onSelect()
        lb.pack(pady=15)  # размещение виджета listbox в главной рамке
        lbl = Label(self, text=0, textvariable=self.var)  # создаем ярлык для отображения выбранного элемента
        lbl.pack()  # размещение ярлыка с помощью менеджера геометрии pack

    def on_select(self, val):
        """
        Метод обработки события из виджета listbox
        :param val: параметр для передачи отправителя события.
        """
        sender = val.widget  # получение отправителя события - listbox со списком
        idx = sender.curselection()  # получение индекса элемента списка в listbox с помощью метода curselection()
        value = sender.get(idx)  # извлечение значения из listbox по индексу с помощью метода get()
        self.var.set(value)  # передача значения в переменную для последующего отображения на ярлыке


def main():
    """
    Функция запуска кода верхнего уровня
    """
    root = Tk()  # создание главного окна приложения
    app = Example(root)  # создание экземпляра приложения с передачей ссылки на главное окно
    root.geometry('300x250+300+300')  # задаем размер окна и его расположение
    root.mainloop()  # запуск основного цикла главного окна


if __name__ == '__main__':  # данная конструкция предотвращает запуск main при импортировании данного файла как модуля
    main()
