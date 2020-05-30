import tkinter
from tkinter import *
from functools import partial   #used for performing calculation

win = Tk()

#l=Label(win,text='username')
#l.pack()
#e=Entry(win)
#e.pack()
#t=Text(win)
#t.insert(INSERT ,'hello')
#t.pack()

def sum(label,x1,x2):
	n1= (x1.get())       #to get the values from the entry
	n2= (x2.get())
	sum=int(n1) + int(n2)
	label.config(text='sum is : %d' %sum)
	return 


l1=Label(win , text='First no. ')
l1.grid(row=1 , column=0)

l2=Label(win , text='Second no. ')
l2.grid(row=2 , column=0)
label=Label(win)
label.grid(row=6 , column=2)

x1=StringVar()
x2=StringVar()

e1=Entry(win, textvariable=x1)
e1.grid(row=1,column=2)

e2=Entry(win, textvariable=x2)
e2.grid(row=2,column=2)

sum=partial(sum,label,x1,x2)

button=Button(win, text='calculate' , command=sum)
button.grid(row=3, column=0)

win.mainloop()