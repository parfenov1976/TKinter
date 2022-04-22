"""
Пример создания меток с помощью виджета Label
"""
import tkinter as tk

window = tk.Tk()
label = tk.Label(
    text="Привет, TKinter!",
    foreground='white',  # цвет шрифт, можно использовать сокращение fg
    background='black',  # цвет фона поля строки, не окна! можно использовать сокращение bg
    width=20,  # ширина поля строки - размеры измеряются в текстовых юнитах, т.е. в знакоместах
    height=20  # высота поля строки
    )
label1 = tk.Label(text='Привет, TKinter!', bg='#34A2FE')  # можно использовать 16ричные коды цветов
label.pack()
label1.pack()
window.mainloop()
