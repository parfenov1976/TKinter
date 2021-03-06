"""
Пример создания кнопки выхода
"""
import tkinter as tk
import tkinter.ttk as ttk


class Example(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)  # создаем кадр в корневом окне, переданном по ссылке
        self.parent = parent  # сохраняем ссылку на родительский виджет, которым является корневое окно
        self.style = ttk.Style()  # создаем стили для виджетов
        self.style.theme_use("default")  # применяем к виджетам стиль по умолчанию (есть еще стили alt и classic)
        self.init_ui()  # вызываем метод, создающий пользовательский интерфейс

    def init_ui(self):
        self.parent.title("Кнопка выхода из приложения")  # задаем заголовок окну через ссылку на родительский виджет
        self.pack(fill=tk.BOTH, expand=1)  # применяем менеджер геометрии
        quit_button = ttk.Button(self, text='Выход', command=self.quit)  # создаем виджет кнопки
        quit_button.place(x=50, y=50)  # располагаем кнопку в окне относительно верхнего левого угла


def main():
    root = tk.Tk()  # создаем корневое окно
    root.geometry("250x150+300+300")  # задаем размер окна и его расположение
    Example(root)  # Инициализация класса приложения
    root.mainloop()  # запуск основного цикла


if __name__ == '__main__':
    main()
