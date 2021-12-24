import tkinter as tk

window = tk.Tk()
label = tk.Label(text='Имя')
# entry = tk.Entry(fg='yellow', bg='blue', width=25)
entry = tk.Entry()
label.pack()
entry.pack()

window.mainloop()
