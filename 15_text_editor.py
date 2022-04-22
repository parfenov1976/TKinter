"""
Пример приложения текстовый редактор с примером открытия диалогового окна на открытие файла,
добавление в окно приложения полосы прокрутки и многострочного текстового поля.
Применены виджеты Frame, Button, Scrollbar, Text. С применением менеджера геометрии grid.

"""
import tkinter as tk
# импорт диалоговых окон для открытия и сохранения файла
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Открывает файл для редактирования"""
    filepath = askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Простой текстовый редактор - {filepath}")


def save_file():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Простой текстовый редактор - {filepath}")


window = tk.Tk()
window.title("Простой текстовый редактор")

# window.rowconfigure(0, minsize=600, weight=1)  # установки минимальной высоты строки 800 пикселей
# window.columnconfigure(1, minsize=800, weight=1)  # установки минимальной ширины столбца 800 пикселей
window.rowconfigure(0, weight=1)  # если minsize не указано, то высоту текстового поля можно будет менять полностью
window.columnconfigure(1, weight=1)  # если minsize не указано, то ширину текстового поля можно будет менять полностью

sb_vertical = tk.Scrollbar(window, orient=tk.VERTICAL)  # добавление вертикальной полосы прокрутки

txt_edit = tk.Text(window, yscrollcommand=sb_vertical.set)  # создание текстового поля в окне и связывание с прокруткой
"""
дополнительные параметры виджета Text:
height = int:screen_units - устанавливает начальную высоту поля, по умолчанию стоит что-то около 30
height = int:screen_units - устанавливает начальную ширину поля, по умолчанию стоит что-то около 100
wrap=str: 'word', 'char', 'none' - управляет переносом строки, по умолчанию стоит char, т.е. по символам
"""

sb_vertical.config(command=txt_edit.yview)  # определение действия для полосы прокрутки
fr_buttons = tk.Frame(window)  # создание фрейма кнопок в окне
btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file)  # создание кнопки в фрейме кнопок
btn_save = tk.Button(fr_buttons, text="Сохранить как...", command=save_file)  # создание кнопки в фрейме кнопок

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)  # создание сетки для фрейма кнопок и размещение кнопки
btn_save.grid(row=1, column=0, sticky="ew", padx=5)  # создание сетки для фрейма кнопок и размещение кнопки
fr_buttons.grid(row=0, column=0, sticky="ns")  # создание сетки для окна и размещение фрейма кнопок в окне
txt_edit.grid(row=0, column=1, sticky="nsew")  # создание сетки для окна и размещение текстового поля в окне
sb_vertical.grid(row=0, column=2, sticky="ns")  # создание столбца сетки и размещение полосы прокрутки

window.mainloop()
