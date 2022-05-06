"""
Пример работы с мышью и клавиатурой
"""

from tkinter import *


class MyLine:
    def __init__(self, line_id, start_x, start_y):
        self.id = line_id
        self.start_x = start_x
        self.start_y = start_y


line_under_creation = MyLine(0, 0, 0)


def key_press_handler(event):
    print(event.char, 'код =', event.keycode)


def mouse_button1_press_handler(event):
    # создаём новую линию
    global line_under_creation
    canvas = event.widget
    line_id = canvas.create_line(event.x, event.y, event.x, event.y)
    line_under_creation = MyLine(line_id, event.x, event.y)


def mouse_button1_release_handler(event):
    global line_under_creation
    line_under_creation = None
    return event  # заглушка от warning из-за неиспользования параметра event


def mouse_motion_handler(event):
    global line_under_creation
    canvas = event.widget
    if event.state == 264:  # Почему 264 при зажатой ЛКМ? В примере было 256. Почему 8 при не нажатых кнопках?
        # зажата левая кнопка мышки - меняем создаваемую линию
        canvas.delete(line_under_creation.id)
        line_id = canvas.create_line(line_under_creation.start_x,
                                     line_under_creation.start_y,
                                     event.x, event.y)
        line_under_creation.id = line_id


root = Tk()
main_frame = Frame(root)
canv = Canvas(main_frame, bg='white', cursor='pencil')
canv["width"] = 600
canv["height"] = 600
root.bind("<KeyPress>", key_press_handler)  # Canvas, Frame не поддерживают bind на клавиатуру
canv.bind("<Motion>", mouse_motion_handler)
canv.bind("<ButtonPress-1>", mouse_button1_press_handler)  # ButtonPress = Button
canv.bind("<ButtonRelease-1>", mouse_button1_release_handler)
canv.pack()
main_frame.pack()
canv.focus()
root.mainloop()
