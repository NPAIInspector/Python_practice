from tkinter import *
from tkinter import messagebox as mb


win = Tk()

mylabel = Label(win, text = "名前を入力して下さい。")
mylabel.pack()

text = Entry(win)
text.pack()
text.insert(END, "  ")

def ok_click():
    a = text.get()
    mb.showinfo("Hi!!",a + "さん、はじめまして!")

okButton = Button(win,text = "ok", command=ok_click)
okButton.pack()

win,mainloop()