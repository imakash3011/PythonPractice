import tkinter 
from tkinter import *

win=Tk()

# mb=Menubutton(win,text='File')
# mb.grid()

# mb.menu = Menu(mb)
# mb['menu']=mb.menu

# x1=IntVar()
# x2=IntVar()

# mb.menu.add_checkbutton(label='open',variable=x1)
# mb.menu.add_checkbutton(label='close',variable=x2)

# mb.pack()


def nothing():
	file=Toplevel(win)
	button=Button(file,text='do nothing')
	button.pack()
menubar=Menu(win)
filemenu = Menu(menubar)
filemenu.add_command(label='New Window' , command=nothing)
filemenu.add_command(label='open' , command=nothing)
filemenu.add_command(label='close' , command=nothing)
filemenu.add_separator()
filemenu.add_command(label='New file' , command=nothing)
filemenu.add_command(label='save' , command=nothing)
filemenu.add_command(label='save as' , command=nothing)
filemenu.add_separator()
filemenu.add_command(label='edit' , command=nothing)
filemenu.add_command(label='close all tab' , command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Exit' , command=win.quit)

menubar.add_cascade(label='File' , menu=filemenu)

editmenu=Menu(menubar)
editmenu = Menu(menubar)
editmenu.add_command(label='Undo' , command=nothing)
editmenu.add_command(label='Redo' , command=nothing)
filemenu.add_separator()
editmenu.add_command(label='Copy' , command=nothing)
editmenu.add_command(label='Paste' , command=nothing)
editmenu.add_command(label='Select all' , command=nothing)
filemenu.add_separator()
editmenu.add_command(label='Exit' , command=win.quit)

menubar.add_cascade(label='Edit' , menu=editmenu)



win.config(menu=menubar)
win.mainloop()