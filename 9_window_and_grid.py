import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    '''
    i- индекс столбца или строки
    weight- относительная рекация на расширение окна, по умолчанию 0
    minsize- минимальный размер высоты строки или столбца в пикселях
    '''

    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)  # pad добавляет отступ в пикселях фрейма рамки
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)  # pad добавляет отступ в пикселях фрейма рамки

window.mainloop()
