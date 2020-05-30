import tkinter
from tkinter import *

win = Tk()

#crreating an arc
c=Canvas(win, height=250 , width=300 , bg='blue')
coord=10,50,240,210
arc=c.create_arc(coord,start=0 , extent=150 , fill='red')

#creating a line
line=c.create_line(10,10,200,200 , fill='white')

c.pack()
win.mainloop()
