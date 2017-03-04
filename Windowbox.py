#Shirong Zheng    CSC113000
#Windowbox
from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()

"""top=Tk()
L1=Label(top,text="n-sides")
L1.pack(side=LEFT)
E1=Entry(top,bd=5)
E1.pack(side=RIGHT)

L2=Label(top,text="r-degree")
L2.pack(side=BOTTOM)
E2=Entry(top,bd=5)
E2.pack(side=BOTTOM)
top.mainloop()"""
