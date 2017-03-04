#Shirong Zheng     CSC11300
#Project 1

import math
import turtle
from Tkinter import *

def entry_fields():
    print("N-sides:%s\nR-RadialLength:%s" %(L1.get(),L2.get()))
master=Tk()
Label(master,text="N-sides").grid(row=0)
Label(master,text="R-RadialLength").grid(row=1)
L1=Entry(master).grid(row=0,column=1)
L2=Entry(master).grid(row=1,column=1)
Button(master,text='Plot',command=master.quit).grid(row=3,column=0,sticky=W,pady=4)
master.mainloop()

def draw_equilpie(t,n,r):
   polypie(t,n,r)
   t.pu()
   t.fd(r*2+10)
   t.pd()
   t.color("purple")
        
def polypie(t,n,r):
   angle=360.0/n
   for i in range(n):
	   isostri(t,r,angle/2)
	   t.lt(angle)
	   	   	   
def isostri(t,r,angle):
  y=r*math.sin(angle*math.pi/180)
  t.rt(angle)
  t.fd(r)
  t.lt(90+angle) 
  t.fd(2*y)
  t.lt(90+angle)
  t.fd(r)
  t.lt(180-angle)
  t.fillcolor('green')

bob=turtle.Turtle()
bob.pu()
bob.bk(130)
bob.pd()
bob.color("red")
size=70
draw_equilpie(bob,5,size)
size=80
draw_equilpie(bob,6,size)

bob.hideturtle()
turtle.mainloop()



