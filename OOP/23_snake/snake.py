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
    BOARD_WIDTH = 300  # ширина игрового поля
    BOARD_HEIGHT = 300  # высота игрового поля
    DELAY = 100  # величина задержки для регулировки скорости игры
    DOT_SIZE = 10  # размер элементов игры на игровом поле
    MAX_RAND_POS = 27  # константа для ограничения части поля, на котором может появиться яблоко


class Board(tk.Canvas):
    """
    Класс игрового поля на основе супер класса холст (Canvas)
    """
    def __init__(self) -> None:
        """
        Конструктор класс игрового поля
        """
        super().__init__(                                       # вызов конструктора родительского класса
            width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT,   # передача размеров игрового поля в конструктор холста
            background='blue', highlightthickness=0             # указание цвета игрового поля и ширины рамки
        )
        self.init_game()  # вызов метода инициализации игры
        self.pack()  # размещение игрового поля в главной рамке приложения, см класс приложения Snake

    def init_game(self) -> None:
        """
        Метод инициализации игры
        """
        self.in_game = True
        self.dots = 3
        self.score = 0

        # переменные для передвижения змеи
        self.move_x = Cons.DOT_SIZE
        self.move_y = 0

        # стартовые координаты для размещения яблока
        self.apple_x = 100
        self.apple_y = 190

        self.load_images()  # вызов метода загрузки изображения из файла
        self.create_objects()  # вызов метода создания объектов на холсте
        self.locate_apple()  # вызов метода распределения яблок по холсту
        self.bind_all('<Key>', self.on_key_pressed)  # метод холста для проверки нажатия клавиш,
        # вызывающий метод управление змейкой on_key_pressed() с передачей ему события по нажатию клавиш
        self.after(Cons.DELAY, self.on_timer)  # метод холста, по истечении времени DELAY
        # вызывающий метод on_timer() для создания игрового цикла для каждого события таймера


    def load_images(self) -> None:
        """
        Метода загрузки нужных для игры изображений
        """
        try:  # перехват ошибки на случай проблем с загрузкой изображений
            self.idot = PIL.Image.open('dot.png')  # создание объекта изображения из файла
            self.dot = PIL.ImageTk.PhotoImage(self.idot)  # создание фотоизображения из объекта изображения
            self.ihead = PIL.Image.open('head.png')  # создание объекта изображения из файла
            self.head = PIL.ImageTk.PhotoImage(self.ihead)  # создание фотоизображения из объекта изображения
            self.iapple = PIL.Image.open('apple.png')  # создание фотоизображения из объекта изображения
            self.apple = PIL.ImageTk.PhotoImage(self.iapple)  # создание фотоизображения из объекта изображения
        except IOError as e:  # перехват ошибки ввода/вывода на случай проблем с загрузкой изображений
            print(e)  # печать сообщения об ошибке
            sys.exit(1)  # команда на завершение сценария со статусом 1 - ошибка

    def create_objects(self) -> None:
        """
        Метод создание объектов на холсте
        """
        self.create_text(                        # метод холста для создания текста на нем
            30, 10, text=f'Счет: {self.score}',  # координаты текстового поля, строка для текстового поля
            tags='score', fill='white'           # метка текстового поля и цвет шрифта
        )
        self.create_image(                                  # метода холста для создания изображения на нем
            self.apple_x, self.apple_y, image=self.apple,   # координаты изображения и аттрибут с изображением
            anchor=tk.NW, tag='apple'                       # привязка изображения, метка изображения
        )
        self.create_image(50, 50, image=self.head, anchor=tk.NW, tag="head")  # отрисовка головы змейки
        self.create_image(30, 50, image=self.dot, anchor=tk.NW, tag="dot")  # отрисовка элемента тела змейки
        self.create_image(40, 50, image=self.dot, anchor=tk.NW, tag="dot")  # отрисовка элемента тела змейки

    pass   # остановка

    def locate_apple(self) -> None:
        """
        Метода распределения яблок по холсту
        """
        apple = self.find_withtag('apple')
        TODO: доделать
