from tkinter import *

top = Tk()
# Code to add widgets will go here...

top.geometry("500x500")

top['bg']='green'

canvas = Canvas()
canvas.create_line(55, 0, 155, 85)

canvas.pack()
top.mainloop()