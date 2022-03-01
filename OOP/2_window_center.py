import tkinter as tk


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")  # создаем кадр в корневом окне, переданном по ссылке
        self.parent = parent  # сохраняем ссылку на родительский виджет, которым является корневое окно
        self.parent.title('Окно по центру экрана')  # присваиваем имя окну
        self.pack(fill=tk.BOTH, expand=1)  # применяем менеджер геометрии
        self.center_window()  # вызываем метод, создающий пользовательский интерфейс

    def center_window(self):
        w = 290  # ширина нашего окна
        h = 150  # высота нашего окна
        sw = self.parent.winfo_screenwidth()  # определяем ширину экрана для текущего разрешения
        sh = self.parent.winfo_screenheight()  # определяем высоту экрана для текущего разрешения
        x = (sw - w) / 2  # рассчитываем положение левого верхнего угла по ширине
        y = (sh - h) / 2  # рассчитываем положение левого верхнего угла по высоте
        self.parent.geometry(f'{w}x{h}+{int(x)}+{int(y)}')  # задаем размер окна и его расположение


def main():
    root = tk.Tk()  # создаем корневое окно
    Example(root)  # Инициализация класса приложения
    root.mainloop()  # запуск основного цикла


if __name__ == '__main__':
    main()
