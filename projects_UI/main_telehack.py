from fileinput import filename
import os
from tkinter import *
from tkinter import filedialog
from pathlib import Path
#import script
import tkinter as tk
import threading
import webbrowser

window = Tk()
window.title("Программа для проверки сайтов")
window.geometry('960x480')
window.resizable(width=False, height=False)
global background
global src_file
global protocol
global noprotocol
global check_l
global access_data
global name
global dir
dir = os.path.abspath(os.curdir)
background = PhotoImage(file = dir + r"\background.png")
background_label = Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def click_btn():
    global filename
    filename = filedialog.askopenfilename()
    if (filename != '' and Path(filename).suffix == '.txt'):
        btn.configure(bg = 'green', fg= 'white')
        btn["text"] = f"Файл загружен"
        btn2["state"] = ACTIVE
        return filename
    else:
        btn.configure(bg = 'red', fg= 'white')
        btn["text"] = f"Неверный формат или не выбран файл"
        btn2["state"] = DISABLED
        return ''

def thread(fn):
        def execute(*args, **kwargs):
            threading.Thread(target=fn, args=args, kwargs=kwargs, daemon= True).start()
        return execute

@thread   
def click_btn1():
    btn2["text"] = f"Проверка..."
    btn["state"] = DISABLED
    btn.configure(bg = 'white', fg= 'black')
    btn2["state"] = DISABLED
    access_data = script.main_script(filename)
    protocol = access_data[0][1]
    noprotocol = access_data[0][0]
    if (access_data):
        btn2['text'] = f'Тест завершён'
        second_window = tk.Toplevel(window)
        second_window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
        second_window.title("Результат теста")
        second_window.geometry('960x480')
        second_window.resizable(width=False, height=False)
        background1 = PhotoImage(file = dir + r"\background.png")
        background1_label = Label(second_window, image=background1)
        background1_label.place(x=0, y=0, relwidth=1, relheight=1)
        def coordinates(x,y):
            if (y == 3):
                script.save_data(filename)
            if (y == 2):
                webbrowser.open('http://' +access_data[1][x], new=0, autoraise=True)
            if (y == 1):
                screenshot = Image.open("img/" + access_data[1][x] + ".png")
                screenshot.show("img/" + access_data[1][x] + ".png")
            if (y == 0):
                trace_window = Toplevel()
                trace_window.title("Результат трассировки")
                trace_window.geometry("640x600")
                trace_window.protocol("WM_DELETE_WINDOW", lambda: trace_window.destroy())
                label = tk.Label(trace_window, text = access_data[2][x])
                label.pack(anchor=CENTER, expand=1)
        #Удачные
        tk1 = tk.Label(second_window,width= 10, height= 1, text="Успешно:", font='Times 11').grid(row = 0, column=0, padx = 0, pady = 5)
        for i in range(protocol):
            tk.Label(second_window,width= 10, height= 1, text=access_data[1][i], font='Times 11').grid(row = i+1, column=0, padx = 15, pady = 5)
            for k in range(3):
                tk.Button(second_window, width= 5, height= 1,text = k+1 ,command=lambda x=i,y=k: coordinates(x,y)).grid(row=i+1,column=k+1, padx = 3, pady = 5)
        k = 0
        #Неудачные
        j = i+1
        tk2 = tk.Label(second_window,width= 10, height= 1, text="Неуспешно:", font='Times 11').grid(row = i+2, column=0, padx = 15, pady = 5)
        for i in range(j,j+noprotocol):
            tk.Label(second_window,width= 10, height= 1, text=access_data[1][i], font='Times 11').grid(row = i+3, column=0, padx = 15, pady = 5)
            for k in range(3):
                tk.Button(second_window, width= 5, height= 1,text = k+1,command=lambda x=i,y=k: coordinates(x,y)).grid(row=i+3,column=k+1, padx = 0, pady = 5)
        tk.Button(second_window, width = 25, height = 5, text= 'Сохранить результат', relief = 'flat',command=lambda x=i+1,y=k+1: coordinates(x,y)).grid(row =i+4,column= k+2, padx = 15, pady= 5)
btn = Button(window,width= 35, height= 5, text="Выбор файла с сайтами",command=click_btn,relief = 'flat') 
btn.grid(column=1, row=1, padx = 150, pady = 300) 
btn2 = Button(window ,width= 25, height= 5, text="Начать тестирование",state = DISABLED, command=click_btn1,relief = 'flat')  
btn2.grid(column=2, row=1, padx = 150, pady = 300)  
window.mainloop()