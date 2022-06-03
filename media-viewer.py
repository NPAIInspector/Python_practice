from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('photo viewer')

photo01 = ImageTk.PhotoImage(Image.open("image01.png"))

my_label = Label(image=photo01)
my_label.grid(row=0, column=0, columnspan=3) 

button_exit =Button(root, text="Quit", command=root.quit)
button_exit.grid(row=1, column=1)

root.mainloop()