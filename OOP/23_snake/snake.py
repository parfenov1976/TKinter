"""
Игра змейка. В этой игре игрок управляет змейкой.
Цель игры – съесть как можно больше яблок.
После каждого съеденного яблока тело змеи увеличивается.
Во время движения змейка должна уклоняться от стен и собственного тела.
https://python-scripts.com/snake-game-python-tkinter
"""

import sys
import random
import PIL.Image
import PIL.ImageTk
import tkinter as tk


class Cons:
    """
    Класс для хранения констант игры
    """
    BOARD_WIDTH = 600  # ширина игрового поля
    BOARD_HEIGHT = 600  # высота игрового поля
    DELAY = 100  # величина задержки для регулировки скорости игры
    DOT_SIZE = 20  # размер элементов игры на игровом поле
    MAX_RAND_POS = 27  # константа для ограничения части поля, на котором может появиться яблоко


class Board(tk.Canvas):
    """
    Класс игрового поля на основе супер класса холст (Canvas)
    """

    def __init__(self) -> None:
        """
        Конструктор класс игрового поля
        """
        super().__init__(  # вызов конструктора родительского класса
            width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT,  # передача размеров игрового поля в конструктор холста
            background='blue', highlightthickness=0  # указание цвета игрового поля и ширины рамки
        )
        self.in_game = True
        self.game_pause = False
        self.timer_id = None
        self.dots = 3
        self.score = 0
        # переменные для передвижения змеи
        self.move_x = Cons.DOT_SIZE
        self.move_y = 0
        # стартовые координаты для размещения яблока
        self.apple_x = 160
        self.apple_y = 80
        try:  # перехват ошибки на случай проблем с загрузкой изображений
            self.idot = PIL.Image.open(r'data\dot.png')  # создание объекта изображения из файла
            self.dot = PIL.ImageTk.PhotoImage(self.idot)  # создание фотоизображения из объекта изображения
            self.ihead = PIL.Image.open(r'data\head.png')  # создание объекта изображения из файла
            self.head = PIL.ImageTk.PhotoImage(self.ihead)  # создание фотоизображения из объекта изображения
            self.iapple = PIL.Image.open(r'data\apple.png')  # создание фотоизображения из объекта изображения
            self.apple = PIL.ImageTk.PhotoImage(self.iapple)  # создание фотоизображения из объекта изображения
        except IOError as e:  # перехват ошибки ввода/вывода на случай проблем с загрузкой изображений
            print(e)  # печать сообщения об ошибке
            sys.exit(1)  # команда на завершение сценария со статусом 1 - ошибка
        self.pack()  # размещение игрового поля в главной рамке приложения, см класс приложения Snake
        self.init_game()  # вызов метода инициализации игры

    def init_game(self) -> None:
        """
        Метод инициализации игры
        """
        self.create_objects()  # вызов метода создания объектов на холсте
        self.locate_apple()  # вызов метода распределения яблок по холсту
        self.bind_all('<Key>', self.on_key_pressed)  # метод холста для проверки нажатия клавиш,
        # вызывающий метод управление змейкой on_key_pressed() с передачей ему события по нажатию клавиш
        self.after(Cons.DELAY, self.on_timer)  # метод холста, по истечении времени DELAY
        # вызывающий метод on_timer() для создания игрового цикла для каждого события таймера

    def create_objects(self) -> None:
        """
        Метод создание объектов на холсте
        """
        self.create_text(  # метод холста для создания текста на нем
            30, 10, text=f'Счет: {self.score}',  # координаты текстового поля, строка для текстового поля
            tags='score', fill='white'  # метка текстового поля и цвет шрифта
        )
        self.create_image(  # метода холста для создания изображения на нем
            self.apple_x, self.apple_y, image=self.apple,  # координаты изображения и аттрибут с изображением
            anchor=tk.NW, tag='apple'  # привязка изображения, метка изображения
        )
        self.create_image(100, 100, image=self.head, anchor=tk.NW, tag="head")  # отрисовка головы змейки
        self.create_image(80, 100, image=self.dot, anchor=tk.NW, tag="dot")  # отрисовка элемента тела змейки
        self.create_image(60, 100, image=self.dot, anchor=tk.NW, tag="dot")  # отрисовка элемента тела змейки

    def check_apple_collision(self) -> None:
        """
        Метод для проверки условия столкновения головы змеи с яблоком
        """
        apple = self.find_withtag('apple')  # находим яблоко на холсте методом холста по тэгу картинки
        head = self.find_withtag('head')  # находи голову змеи методом холста по тэгу картинки
        x1, y1, x2, y2 = self.bbox(*head)  # извлечение точек границ изображения головы и присвоение их переменным
        overlap = self.find_overlapping(x1, y1, x2, y2)  # поиск и сборка объектов наложившихся на изображение головы
        for ovr in overlap:  # перебор найденных по результатам поиска наложений объектов
            if apple[0] == ovr:  #
                self.score += 1  # увеличение счета если яблоко было съедено
                x, y = self.coords(apple)  # извлечение координат яблока
                self.create_image(x, y, image=self.dot, anchor=tk.NW, tag='dot')  # добавление сегмента
                # в тело змейки, если яблоко было съедено по координатам яблока
                self.locate_apple()  # вызов метода замены яблока

    def move_snake(self):
        """
        Метод, перемещающий змейку по холсту
        """
        dots = self.find_withtag('dot')  # находим тело змейки на холсте методом холста по тэгу картинки
        head = self.find_withtag('head')  # находим голову змейки на холсте методом холста по тэгу картинки
        items = dots + head  # собираем змейку в единый объект
        z = 0
        while z < len(items) - 1:
            """
            Данный цикл обеспечивает движение частей змейки одной цепью
            """
            x1, y1 = self.coords(items[z])  # извлечение координат текущего элемента
            x2, y2 = self.coords(items[z + 1])  # извлечение координат следующего элемента
            self.move(items[z], x2 - x1, y2 - y1)  # перемещение текущего элемента
            z += 1  # увеличение индекса
        self.move(head, self.move_x, self.move_y)  # изменение направления движения змейки после
        # после каждого нажатия клавиш

    def check_collisions(self):
        """
        Метод проверки на столкновения змеи с другими объектами
        """
        dots = self.find_withtag('dot')  # находим тело змейки на холсте методом холста по тэгу картинки
        head = self.find_withtag('head')  # находим голову змейки на холсте методом холста по тэгу картинки
        x1, y1, x2, y2 = self.bbox(*head)  # извлечение точек границ изображения головы и присвоение их переменным
        overlap = self.find_overlapping(x1, y1, x2, y2)  # создание перечня изображений на которые
        # накладывается изображение головы
        for dot in dots:  # перебор элементов тела
            for over in overlap:  # перебор элементов перечня наложения
                if over == dot:  # проверка равенства элемента тела и элемента из списка наложения
                    self.in_game = False  # флаг продолжения игры
        if x1 < 0:  # условие столкновения головы с левой границей поля
            self.in_game = False  # флаг продолжения игры
        if x1 > Cons.BOARD_WIDTH - Cons.DOT_SIZE:  # условие столкновения головы с правой границей поля
            self.in_game = False  # флаг продолжения игры
        if y1 < 0:  # условие столкновения головы с верхней границей поля
            self.in_game = False  # флаг продолжения игры
        if y1 > Cons.BOARD_HEIGHT - Cons.DOT_SIZE:  # условие столкновения головы с нижней границей поля
            self.in_game = False  # флаг продолжения игры

    def locate_apple(self) -> None:
        """
        Метода распределения яблок по холсту - устанавливает новое яблоко в случайной точке
        и удаляет старое яблоко с игровой карты
        """
        apple = self.find_withtag('apple')  # находим изображение яблоко на холсте по тэгу
        self.delete(apple[0])  # удаляем яблоко с игрового поля методом холста delete()
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.apple_x = r * Cons.DOT_SIZE
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.apple_y = r * Cons.DOT_SIZE
        self.create_image(  # метода холста для создания изображения на нем
            self.apple_x, self.apple_y, image=self.apple,  # координаты изображения и аттрибут с изображением
            anchor=tk.NW, tag='apple'  # привязка изображения, метка изображения
        )

    def on_key_pressed(self, e: tk.Event) -> None:
        """
        Метод управления змейкой с помощью стрелок клавиатуры
        """
        left_cursor_key = 'Left'  # создание переменной для хранения соответствия клавише
        right_cursor_key = 'Right'
        up_cursor_key = 'Up'
        down_cursor_key = 'Down'
        esc = 'Escape'
        space = 'space'
        key = e.keysym  # извлечение строки названия нажатой клавиши из объекта события
        if key == left_cursor_key and self.move_x <= 0:  # проверка соответствия названия нажатой клавиши и переменной
            # проверка координаты обеспечивает продолжение безостановочное движения когда клавиша отпущена
            self.move_x = -Cons.DOT_SIZE  # изменение координаты объекта
            self.move_y = 0
        if key == right_cursor_key and self.move_x >= 0:
            self.move_x = Cons.DOT_SIZE
            self.move_y = 0
        if key == up_cursor_key and self.move_y <= 0:
            self.move_x = 0
            self.move_y = -Cons.DOT_SIZE
        if key == down_cursor_key and self.move_y >= 0:
            self.move_x = 0
            self.move_y = Cons.DOT_SIZE
        if key == esc:
            self.game_pause = not self.game_pause
            self.pause_menu()
        if key == space and not self.in_game:
            self.new_game()

    def on_timer(self) -> None:
        """
        Метод для создания игрового цикла для каждого события таймера
        """
        if self.in_game:  # проверка условия продолжения игры
            self.draw_score()  # вызов метода отрисовки счета
            self.check_collisions()  # вызов метода проверки столкновений змейки с другими объектами
            self.check_apple_collision()  # вызов метода проверки столкновения головы змейки с яблоком
            self.move_snake()  # вызов метода перемещения змейки
            self.timer_id = self.after(Cons.DELAY, self.on_timer)  # метод холста?, который запускает метод после
            # истечения таймера один раз, поэтому вызывается рекурсивно в методе on_timer()
            # self.after() возвращает id запланированной к запуску функции
        else:
            self.game_over()  # вызов метода завершения игры если условие продолжения игры ложь

    def pause_menu(self):
        if self.game_pause and self.in_game:
            self.after_cancel(self.timer_id)  # отмена запуска запланированной функции
            self.create_text(  # метод холста для создания текста на нем
                self.winfo_width() / 2, self.winfo_height() / 2,  # координаты текстового поля
                text=f'Счет: {self.score}\n\n ПАУЗА',  # строка для текстового поля
                tags='pause', fill='white'  # метка текстового поля и цвет шрифта
            )
        else:
            self.delete('pause')
            self.after(Cons.DELAY, self.on_timer)  # перезапуск игрового цикла

    def draw_score(self) -> None:
        """
        Метод отрисовки счета игры
        """
        score = self.find_withtag('score')
        self.itemconfig(*score, text=f'Счёт: {self.score}')

    def game_over(self) -> None:
        """
        Метод завершения игры - удаляет все объекты и выводит сообщение об окончании игры
        """
        self.delete(tk.ALL)  # метод холста для удаления всех объектов с него
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2,
                         text=f'{" "*12}Игра закончена со счетом {self.score}\n\nнажмите Пробел для начала новой игры',
                         tags='game_over', fill='white')
        # Создание сообщения об окончании игры с помощью метода холста.
        # Извлечение размеров окна с помощью методом winfo.

    def new_game(self) -> None:
        self.destroy()
        self.__init__()


class Snake(tk.Frame):
    """
    Класс приложения с наследованием от супер класса рамки
    """

    def __init__(self, parent: tk.Tk) -> None:
        """
        Конструктор класса приложения
        """
        tk.Frame.__init__(self)  # вызов конструктора супер класса рамки
        self.parent = parent  # сохранение ссылка на главное окно приложения в аттрибуте приложения
        self.parent.title('Змейка')  # присвоение имени главному окну приложения
        self.board = Board()  # создание экземпляра игрового поля
        self.pack()  # размещение рамки приложения в главном окне


def main() -> None:
    """
    Функция с кодом приложения верхнего уровня
    """
    root = tk.Tk()  # создание главного окна приложения
    Snake(root)  # создание объекта приложения с передачей ссылки на главное окно приложения
    root.resizable(False, False)  # запрет на изменение размеров окна
    root.mainloop()  # запуск главного цикла приложения


if __name__ == '__main__':  # условия проверки для предотвращения запуска кода верхнего уровня при импортировании
    # данного файла как модуля
    main()  # вызов функции с кодом верхнего уровня
