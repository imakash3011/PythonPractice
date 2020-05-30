import tkinter
from tkinter import *
from tkinter import messagebox

win = Tk()
#frame=Frame(win)
#frame.pack()

# frame2=Frame(win)
# frame2.pack()

#rb is in frame and frame is in  windows
# rb=Button(frame,text='Red' , fg='red')
# rb.pack(side=LEFT)
# bb=Button(frame,text='Blue' , fg='blue')
# bb.pack(side=LEFT)
# blb=Button(frame,text='Black' , fg='black')
# blb.pack(side=LEFT)

# gb=Button(frame2,text='Green' , fg='green')
# gb.pack(side=BOTTOM)



# lb=Listbox(win)
# lb.insert(1,'Python')
# lb.insert(2,'Java')
# lb.insert(3,'C')
# lb.insert(4,'C++')
# lb.insert(5,'Jquery')
# lb.insert(6,'Ruby')
# lb.pack()

#multiple windows
# win.title('first')
# top=Toplevel()
# top.title('second')

#creating a popup message
def hello():
	messagebox.showinfo('from computer','hey there')
b=Button(win,text='popup' , command=hello)
b.pack()

win.mainloop()