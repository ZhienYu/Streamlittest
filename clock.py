from tkinter import * 
from tkinter.ttk import *
from time import strftime

myclock = Tk()
myclock.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(myclock, font=("Arial Rounded Bold", 80))
label.pack(anchor = 'center')
time()
mainloop()