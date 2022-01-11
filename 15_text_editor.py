import tkinter as tk

window = tk.Tk()
window.title("Простой текстовый редактор")

window.rowconfigure(0, minsize=800, weight=1)  # установки минимальной высоты строки 800 пикселей
window.columnconfigure(1, minsize=800, weight=1)  # установки минимальной ширины столбца 800 пикселей

txt_edit = tk.Text(window)  # создание текстового поля в окне
fr_buttons = tk.Frame(window)  # создание фрейма кнопок в окне
btn_open = tk.Button(fr_buttons, text="Открыть")  # создание кнопки в фрейме кнопок
btn_save = tk.Button(fr_buttons, text="Сохранить как...")  # создание кнопки в фрейме кнопок

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)  # создание сетки для фрейма кнопок и размещение кнопки
btn_save.grid(row=1, column=0, sticky="ew", padx=5)  # создание сетки для фрейма кнопок и размещение кнопки

fr_buttons.grid(row=0, column=0, sticky="ns")  # создание сетки для окна и размещение фрейма кнопок в окне
txt_edit.grid(row=0, column=1, sticky="nsew")  # создание сетки для окна и размещение текстового поля в окне

window.mainloop()
