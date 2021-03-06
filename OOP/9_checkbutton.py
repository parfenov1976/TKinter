"""
Пример использования чекбокса
"""

from tkinter import Tk, Frame, Checkbutton, BooleanVar, BOTH, Label


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self)  # вызов конструктора родительского класса для создания рамки
        self.parent = parent  # сохранение ссылки на основное окно
        self.var = BooleanVar()  # создаем объект логических значений для чекбокса
        self.var1 = BooleanVar()
        self.lbl = Label(self, text='ЧИСТО')  # создаем надпись для чб1 с надписью для значения по умолчанию
        self.init_ui()  # вызов метода построения интерфейса

    def init_ui(self):
        self.parent.title('Чекбокс')  # присвоение имени окну приложения
        self.pack(fill=BOTH, expand=True)  # размещение базовой рамки, в которой будут размещаться остальные рамки
        cb = Checkbutton(self, text='Показать заголовок', variable=self.var, command=self.on_click)
        # Создаем чекбокс с надписью, объект логических значений связан с виджетом через параметр variable.
        # При нажатии на чекбокс (установка/снятие галки) вызывается метод on_click
        cb.select()  # по умолчанию устанавливаем галку в чекбокс с помощью метода установки галки
        cb.place(x=50, y=50)  # располагаем чекбокс в рамке
        cb1 = Checkbutton(self, variable=self.var1, command=self.on_click1)
        # cb1.select()  # по умолчанию галка не установлена, т.к. метод закомментирован и не вызывается
        # можно явно снять галку с помощью метода deselect()
        cb1.deselect()  # по умолчанию снимаем галку в чекбокс с помощью метода снятия галки
        cb1.place(x=50, y=100)
        self.lbl.pack()  # располагаем чекбокс в рамке

    def on_click(self):
        """
        Метод, вызываемый при нажатии на чекбокс
        """
        if self.var.get():  # проверка содержимого объекта логических значений
            self.parent.title('Чекбокс')  # установка имени окна
        else:
            self.parent.title('')  # установка пустого имени окна

    def on_click1(self):
        """
        Метод, вызываемый при нажатии на чекбокс1
        """
        if self.var1.get():  # проверка содержимого объекта логических значений
            self.lbl['text'] = 'УСТАНОВЛЕНО'  # установка значения надписи при установленной галке
        else:
            self.lbl['text'] = 'ЧИСТО'  # установка значения надписи при снятой галке


def main():
    root = Tk()  # создание главного окна приложения
    root.geometry('250x150+300+300')  # указание положения главного окна и его размеров
    app = Example(root)  # создание экземпляра приложения с передачей ссылка на главное окно
    root.mainloop()  # запуск основного цикла главного окна


if __name__ == '__main__':
    main()
