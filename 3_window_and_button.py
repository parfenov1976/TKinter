import tkinter as tk

window = tk.Tk()
button = tk.Button(
    text="Нажми на меня!",
    fg='yellow',  # цвет шрифт, можно использовать сокращение fg
    bg='blue',  # цвет фона поля строки, не окна! можно использовать сокращение bg
    width=25,  # ширина поля строки - размеры измеряются в текстовых юнитах, т.е. в знакоместах
    height=5  # высота поля строки
    )

button.pack()
window.mainloop()
