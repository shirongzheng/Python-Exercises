#Project 2-Pie Chart

import tkMessageBox
import math
import string
from turtle import*
from Tkinter import *

def entry_fields():
    print("# of first letters to display(%):%s\n# of first letters to display(%):%s" %(L1.get(),L2.get()))
master=Tk()
Label(master,text="# of first letters to display(%):").grid(row=0)
Label(master,text="# of second letters to display(%):").grid(row=1)
L1=Entry(master).grid(row=0,column=1)
L2=Entry(master).grid(row=1,column=1)
Button(master,text='Plot',command=master.quit).grid(row=3,column=0,sticky=W,pady=4)
master.mainloop()

chart_title = 'N Most Frequent Letters In Words.txt File'
segment_labels = ['QLD', 'VIC', 'NSW', 'SA', 'WA', 'TAS', 'NT', 'ACT']
percentages = [0.084, 0.016, 0.019, 0.034, 0.103, 0.0211, 0.0158, 0.0523,0.053,0.00103,0.0058,
0.035,0.026,0.056,0.065,0.00061,0.0502,0.051,0.066,0.024,0.0103,0.0213,0.00088,0.0203,0.00023]

radius = 200

penup()
forward(radius)
left(90)
pendown()
color('palegreen')
begin_fill()
circle(radius)
end_fill()
home()
right(90)
color('black')


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

fp=open('C:\Users\Shirong\My Documents\emma.txt','r')
file_list=fp.readlines()
print file_list
freqs = {}
for line in file_list:
    line = filter(lambda x: x in string.letters, line.lower())
    for char in line:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

print freqs










