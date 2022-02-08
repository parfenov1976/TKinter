import tkinter as tk


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")  # создаем кадр в корневом окне, переданном по ссылке
        self.parent = parent  # сохраняем ссылку на родительский виджет, которым является корневое окно
        self.init_ui()  # вызываем метод, создающий пользовательский интерфейс

    def init_ui(self):
        self.parent.title("Simple")  # задаем заголовок окну через ссылку на родительский виджет
        self.pack(fill=tk.BOTH, expand=1)  # применяем менеджер геометрии


def main():
    root = tk.Tk()  # создаем корневое окно
    root.geometry("250x150+300+300")  # задаем размер окна и его расположение
    app = Example(root)  # Инициализация класса приложения
    root.mainloop()  # запуск основного цикла


if __name__ == '__main__':
    main()
