"""
Пример создания главного окна и использования виджета Label
"""
import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Python рулит!")
greeting.pack()
window.mainloop()
