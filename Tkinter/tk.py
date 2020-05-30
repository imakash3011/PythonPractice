import tkinter 
from tkinter import *

#for creating windows
win=Tk()

#calling function pr
def pr():
	print('hi')

win.geometry("250x300")

#adding button 
b=Button(win , text='button' , command=pr , padx =20 ,pady=20 ,activeforeground='red')
#b.pack()   #to show the button
b.place(x=100 , y=120)


#adding button 
b=Button(win , text='bu')
#b.pack()   #to show the button
b.grid(row=2 , column=2)

win.mainloop()
