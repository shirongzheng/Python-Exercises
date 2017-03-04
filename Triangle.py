#Shirong Zheng    CSC11300
#Triangle

import math
import string
import turtle
import Tkinter 
from turtle import*
from Tkinter import *

a=float(input("The side1 is:"))
b=float(input("The side2 is:"))
c=float(input("The side3 is:"))
class Polygon(object):
    def __init__(self,n):
	    self.number_of_sides=n
    def print_num_sides(self):
	    print('There are'+str(self.number_of_sides)+'sides.')
class Triangle(Polygon):
    def __init__(self,angle1,angle2,angle3):
	    self.angle1=angle1
	    self.angle2=angle2
	    self.angle3=angle3
	    self.number_of_sides=3
    	
    def is_triangle(self):
	    if self.angle1+self.angle2+self.angle3 ==180:
	        return True
	    else: 
		    return False
    
    def area(self):
	    a,b,c=self.lengths_of_sides
	    s=(a+b+c)/2
	    area=(s*(s-a)*(s-b)*(s-c))**0.5
	    return area
    def perimeter(self):
	    a,b,c=self.lengths_of_sides
	    p=a+b+c
	    return p
    turtle.setup(800,600)
    wn=turtle.Screen()
    wn.bgcolor("blue")
    wn.title("tri")
    tri=turtle.Turtle()
    tri.color("red")
    tri.pensize(5)
    tri.fd(320)
    tri.lt(120)
    tri.fd(320)
    tri.lt(120)
    tri.fd(320)
    tri.lt(120)
    
	
class Isosceles(Triangle):
    def __init__(self,lengths_of_sides):
        Polygon.__init__(self,3)
        self.lengths_of_sides=lengths_of_sides
    	
    def is_Isostriangle(self):
	    if self.angle1+self.angle2+self.angle3 ==180:
	        return True
	    else: 
		    return False
    
    def area(self):
	    a,b,c=self.lengths_of_sides
	    s=(a+b+c)/2
	    area=(s*(s-a)*(s-b)*(s-c))**0.5
	    return area
    def perimeter(self):
	    a,b,c=self.lengths_of_sides
	    p=a+b+c
	    return p
	
my_triangle=Triangle(60,50,70)
print my_triangle.number_of_sides
print my_triangle.is_triangle()
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle is %0.2f" %area)
perimeter=a+b+c
print("The perimeter of triangle is %0.2f" %perimeter)


tri1=Isosceles([100,100,72])
print(tri1.area())
print(tri1.perimeter())
a = 100
b = 100
c = 72
def angle (a, b, c):
    return math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))
angA = angle(a,b,c)
angB = angle(b,c,a)
angC = angle(c,a,b)
assert angA + angB + angC == 180.0
print angA
print angB
print angC
turtle.setup(800,600)
wn=turtle.Screen()
wn.bgcolor("green")
wn.title("tri1")
tri1=turtle.Turtle()
tri1.color("purple")
tri1.pensize(7)
tri1.fd(320)
tri1.lt(120)
tri1.fd(320)
tri1.lt(120)
tri1.fd(320)
tri1.lt(120)


tri2=Isosceles([100,100,100*sqrt(2)])
print(tri2.area())
print(tri2.perimeter())
turtle.setup(800,600)
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("tri2")
tri2=turtle.Turtle()
tri2.color("blue")
tri2.pensize(8)
tri2.fd(320)
tri2.lt(120)
tri2.fd(320)
tri2.lt(120)
tri2.fd(320)
tri2.lt(120)
a = 100
b = 100
c = 100*sqrt(2)
def angle (a, b, c):
    return math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))
angA = angle(a,b,c)
angB = angle(b,c,a)
angC = angle(c,a,b)
assert angA + angB + angC == 180.0
print angA
print angB
print angC

tri3=Isosceles([100,50,50])
print(tri3.area())
print(tri3.perimeter())
turtle.setup(800,600)
wn=turtle.Screen()
wn.bgcolor("purple")
wn.title("tri3")
tri3=turtle.Turtle()
tri3.color("yellow")
tri3.pensize(9)
tri3.fd(320)
tri3.lt(120)
tri3.fd(320)
tri3.lt(120)
tri3.fd(320)
tri3.lt(120)
a = 100
b = 50
c = 50
def angle (a, b, c):
    return math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))
angA = angle(a,b,c)
angB = angle(b,c,a)
angC = angle(c,a,b)
assert angA + angB + angC == 180.0
print angA
print angB
print angC

class PieChart(Triangle):
    chart_title = 'N Most Frequent Letters In Words.txt File'
    segment_labels = ['1','2','3']
    percentages = [0.72,0.90,0.60]
    fillcolor=['blue','red','white']
    radius = 200
    penup()
    forward(radius)
    left(90)
    pendown()
    color('yellow')
    begin_fill()
    circle(radius)
    end_fill()
    home()
    right(90)
    color('black')
    write("72,90,60")
    
    def segment(percentages):
        rollingPercent = 0
        radius=200
        for percent in percentages:
            segment = percent * 360
            rollingPercent += segment
            setheading(rollingPercent)
            pendown()
            forward(radius)
            penup()
            home()
    segment(percentages)


	
  
	



