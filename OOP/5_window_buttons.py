import tkinter as tk
import tkinter.ttk as ttk


class Example(ttk.Frame):
    def __init__(self):
        super().__init__()  # вызов конструктора родительского класса
        self.init_ui()

    def init_ui(self):
        self.master.title('Кнопки в tkinter')  # установка имени окна
        self.style = ttk.Style()  # # создаем стили для виджетов
        self.style.theme_use('default')  # применяем к виджетам стиль по умолчанию (есть еще стили alt и classic)
        # ttk.Style().theme_use('default')  # альтернативный способ задать и применить стиль
        frame = ttk.Frame(self, relief=tk.RAISED, borderwidth=1)  # создание основного фрейма
        frame.pack(fill=tk.BOTH, expand=True)  # применяем менеджер геометрии к фрейму
        self.pack(fill=tk.BOTH, expand=True)  # применяем менеджер геометрии к фрейму
        close_button = ttk.Button(self, text='Закрыть')  # создание виджета кнопки
        close_button.pack(side=tk.RIGHT, padx=5, pady=5)  # применение менеджера геометрии
        ok_button = ttk.Button(self, text='Готово')  # создание виджета кнопки
        ok_button.pack(side=tk.RIGHT)  # применение менеджера геометрии


def main():
    root = tk.Tk()  # создание корневого окна приложения
    root.geometry('300x200+300+300')  # размещение корневого окна приложения (текстовые юниты)
    Example()  # Инициализация класса приложения
    root.mainloop()  # запуск основного цикла окна приложения


if __name__ == '__main__':
    main()
