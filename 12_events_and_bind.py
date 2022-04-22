"""
Пример создания события и привязки его к виджету кнопки с помощью метода bind
Закомментирован пример привязки события к нажатию кнопки на клавиатуре
"""
import tkinter as tk

window = tk.Tk()


# __________1 - Нажатие кнопки на клавиатуре
# def handle_keypress(event):
#     print(event.char)
#
#
# window.bind("<Key>", handle_keypress)
# ___________2 - Нажатие на виджет кнопки
def handle_keypress(event):  # event нужен, без него будет вызвано исключение
    print("Нажата кнопка")


button = tk.Button(text="Кликни")
button.pack()

button.bind("<Button-1>", handle_keypress)

window.mainloop()
