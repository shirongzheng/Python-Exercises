#Shirong Zheng    CSC11300
#Square

import turtle
import math

bob=turtle.Turtle()

def square(t):
   for i in range(4):
      t.fd(100)
      t.lt(90)
square (bob)



def polygan(t,n,length):
   angle=350/n
   for i in range(n):
	  t.fd(length)
	  t.lt(angle)
polygan(bob,5,100)


