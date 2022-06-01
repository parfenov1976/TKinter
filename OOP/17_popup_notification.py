"""
Пример создания всплывающих окно с уведомлениями с размещением элементов интерфейса
с помощью менеджера геометрии grid
"""

from tkinter import Tk
from tkinter.ttk import Frame, Button
from tkinter import messagebox as mbox


class Example(Frame):
    """
    Класс главной рамки приложения с наследованием от родительского класса Frame
    """

    def __init__(self, parent):
        """
        Конструктор класса приложения.
        :param parent: параметр для передачи ссылка на главное окно приложения
        """
        Frame.__init__(self, parent)  # запуск конструктора родительского класса
        self.parent = parent  # сохранение ссылки на главное окно приложения в параметрах объекта приложения
        self.ntc_state = None
        self.init_ui()  # вызов метода инициализации графического интерфейса

    def init_ui(self):
        """
        Метод инициализации графического интерфейса приложения
        """
        self.parent.title('Всплывающие окна с уведомлениями')
        self.pack()  # размещение главной рамки приложения в главном окне
        error = Button(self, text='Ошибка', command=self.on_error)  # создание кнопки Ошибка
        error.grid(padx=5, pady=5)  # размещение кнопки в сетке главной рамки
        warning = Button(self, text='Предупреждение', command=self.on_warn)  # создание кнопки Предупреждение
        warning.grid(row=1, column=0)  # размещение кнопки в сетке главной рамки
        question = Button(self, text='Вопрос', command=self.on_quest)  # создание кнопки Вопрос
        question.grid(row=0, column=1)  # размещение кнопки в сетке главной рамки
        inform = Button(self, text='Информация', command=self.on_info)  # создание кнопки Информация
        inform.grid(row=1, column=1)  # размещение кнопки в сетке главной рамки
        can = Button(self, text='Отмена', command=self.on_can)  # создание кнопки Отмена
        can.grid(row=2, column=0)  # размещение кнопки в сетке главной рамки
        yesno = Button(self, text='Да/нет', command=self.on_yesno)  # создание кнопки Да/Нет
        yesno.grid(row=2, column=1)  # размещение кнопки в сетке главной рамки
        retrycancel = Button(self, text='Повторить/Отменить', command=self.on_retrycancel)  # создание кнопки Пов/Отм
        retrycancel.grid(row=3, column=0)  # размещение кнопки в сетке главной рамки
        yesnocancel = Button(self, text='Да/Нет/Отменить', command=self.on_yesnocancel)  # создание кнопки Пов/Отм
        yesnocancel.grid(row=3, column=1)  # размещение кнопки в сетке главной рамки
        prnt = Button(self, text='Печатать последнее состояние', command=self.prnt)
        prnt.grid(row=4, columnspan=2)

    def prnt(self):
        print(self.ntc_state)

    def on_error(self):
        """
        Метод вызова всплывающего окна уведомления об ошибке
        """
        # print(mbox.showerror('Ошибка', 'Не могу открыть файл'))
        # значение mbox можно вернуть или присвоить переменной, аттрибуту объекта для дальнейшей проверке
        self.ntc_state = mbox.showerror('Ошибка', 'Не могу открыть файл')

    def on_warn(self):
        """
        Метод вызова всплывающего окна уведомления с предупреждением
        """
        self.ntc_state = mbox.showwarning('Предупреждение', 'Вызов устаревшей функции')
        print(self.ntc_state)

    @staticmethod
    def on_quest():
        """
        Метод вызова всплывающего окна уведомления с вопросом
        """
        print(mbox.askquestion('Вопрос', 'Вы уверены, что хотите выйти?'))

    @staticmethod
    def on_info():
        """
        Метод вызова всплывающего окна информационного уведомления
        """
        print(mbox.showinfo('Информация', 'Скачивание завершено'))

    @staticmethod
    def on_can():
        """
        Метод вызова всплывающего окна уведомления об отмене
        """
        print(mbox.askokcancel('Отмена-на', 'Отмена действия'))

    @staticmethod
    def on_yesno():
        """
        Метод вызова всплывающего окна уведомления с вопросом
        """
        print(mbox.askyesno('Да-Нет', 'Да или Нет?'))

    @staticmethod
    def on_retrycancel():
        """
        Метод вызова всплывающего окна уведомления с вопросом
        """
        print(mbox.askretrycancel('Повторить-Отменить', 'Повторить или Отменить?'))

    @staticmethod
    def on_yesnocancel():
        """
        Метод вызова всплывающего окна уведомления с вопросом
        """
        print(mbox.askyesnocancel('Да-Нет-Отменить', 'Да/Нет или Отменить?'))


def main():
    """
    Функция для запуска основного цикла приложения
    """
    root = Tk()  # создание главного окно приложения
    app = Example(root)  # создание объекта приложения с передачей ссылки на главное окно приложения
    root.geometry('300x150+300+300')  # установка размеров главного окна и координат его левого верхнего угла
    root.mainloop()  # запуск цикла главного окна приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуск main при импортировании данного файла
    main()
