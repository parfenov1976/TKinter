import tkinter as tk

field_names = ['Имя:',
               'Фамилия:',
               'Адрес1:',
               'Адрес2:',
               'Город:',
               'Регион:',
               'Почтовый индекс:',
               'Страна:']

window = tk.Tk()
window.title("Введите домашний адрес")

frame1 = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frame1.pack(fill=tk.X)
frame1.columnconfigure(0, minsize=105)
frame1.columnconfigure(1, minsize=305)
for i in range(len(field_names)):
    frame1.rowconfigure(i)
    label = tk.Label(master=frame1, text=field_names[i])
    label.grid(row=i, column=0, sticky='e')
ent_width = 50
name_ent = tk.Entry(master=frame1, width=ent_width)
name_ent.grid(row=0, column=1)
surname_ent = tk.Entry(master=frame1, width=ent_width)
surname_ent.grid(row=1, column=1)
address1_ent = tk.Entry(master=frame1, width=ent_width)
address1_ent.grid(row=2, column=1)
address2_ent = tk.Entry(master=frame1, width=ent_width)
address2_ent.grid(row=3, column=1)
town_ent = tk.Entry(master=frame1, width=ent_width)
town_ent.grid(row=4, column=1)
region_ent = tk.Entry(master=frame1, width=ent_width)
region_ent.grid(row=5, column=1)
zipcode_ent = tk.Entry(master=frame1, width=ent_width)
zipcode_ent.grid(row=6, column=1)
country_ent = tk.Entry(master=frame1, width=ent_width)
country_ent.grid(row=7, column=1)

frame2 = tk.Frame()
frame2.pack(fill=tk.X, ipadx=5, ipady=5)

clear_btn = tk.Button(master=frame2, text='Очистить')
clear_btn.pack(side=tk.RIGHT, padx=10, ipadx=10)
send_btn = tk.Button(master=frame2, text='Отправить')
send_btn.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()
