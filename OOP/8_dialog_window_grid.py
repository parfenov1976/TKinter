"""
Пример применения менеджера геометрии grid
"""
from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)  # вызов конструктора родительского класса
        self.parent = parent  # сохранение ссылки на основное окно
        self.init_ui()  # вызов метода построения интерфейса

    def init_ui(self):
        self.parent.title('Диалоговое окно в Tkinter')  # присвоение имени окну приложения
        self.pack(fill=BOTH, expand=True)  # размещение базовой рамки, в которой будут размещаться остальные рамки
        self.columnconfigure(1, weight=1)  # конфигурирование столбцов сетки, weight задает масштаб растягивания
        self.columnconfigure(3, pad=7)  # pad устанавливает отступ между столбцами
        self.rowconfigure(3, weight=1)  # конфигурирование строк сетки
        self.rowconfigure(5, pad=7)  # pad устанавливает отступ между строками
        lbl = Label(self, text="Окна")  # создание надписи
        lbl.grid(sticky=W, pady=4, padx=5)  # размещение надписи над текстовым полем с прикреплением к левому краю
        # padx и pady - отступы снаружи соответственно по горизонтали и вертикали в пикселях от края главного окна
        area = Text(self)  # создание многострочного текстового поля
        area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)
        '''
        выше размещение текстового поля на три столбца (0-2) и на 4 строки (1-4) с внешними отступами по горизонтали
        5 пикселей с прикреплением ко всем сторонам для реализации растягивания при масштабировании окна
        '''
        abtn = Button(self, text='Активир.')  # создание кнопки
        abtn.grid(row=1, column=3)  # размещение кнопки в сетке
        cbtn = Button(self, text='Закрыть')
        cbtn.grid(row=2, column=3, pady=4)
        hbtn = Button(self, text='Помощь')
        hbtn.grid(row=5, column=0, padx=5)
        obtn = Button(self, text='Готово')
        obtn.grid(row=5, column=3)


def main():
    root = Tk()  # создаем главное окно приложения
    root.geometry('350x300+300+300')  # задаем начальное положение окна и его размеры
    app = Example(root)  # создаем экземпляр класса приложения с передачей ссылки на главное окно
    root.mainloop()  # запускаем основной цикл главного окна


if __name__ == '__main__':
    main()
