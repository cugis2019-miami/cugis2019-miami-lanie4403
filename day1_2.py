# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#printing
print("Hello World") #print 

#practicequestion
print("Hello I am learning to code in python") #print 


#calculator
#multiplication
5*2

# division#
5/2

#subtraction#
5-2

#addition#
5+2

#exponent#
5^2

#creating functions
#sum of two numbers

def sum(a,b):
    sum = a + b
    print ("The sum of", a, "and", b, "is", sum)
    
#testingthefunction
sum(3,5.5)

#practice
#create a function which is the sum of three numbers
def sumthree(a,b,c):
    sumthree = a + b + c
    print ("The sum of the numbers", a, "and", b, "and", c, "is", sumthree)
    
sumthree(1,2,3)

#practice create function to calculate the area of a triangle

def areatriangle(base,height):
    area = 0.5*base*height
    print ("The area of the triangle of base", base, "and height", height, "is",area)
 
areatriangle(2,3)

#using libraries
# math library
import math
dir(math) #gives menu of functions available in the math library

#some examples
math.e 

math.pi

math.pow(2,3)

#plotly library for creating graphs
import plotly  #import plotly library

from ploltly.offline import plot
#within the offline function of plotly select the option called plot

import plotly.graph_objs as go  
# import the graph_objs function from the plotly library
#give a proxy name "go" short form for graph objects

#create a Bar graph for the sample data set (1,2), (2,4), (3,3), (2,2).
trace = go.Bar(
        x=[1,2,3,4], y=[2,4,3,2])

plot(data)

#create a line graph
trace = go.Scatter(
        x=[1,2,3,4], y=[2,4,3,2])
data =[trace]
plot(data)

#create a bar graph with colour
trace1 = go.Bar(
        x=["zara","george","ollie","stan"], y=[2,4,3,2],
        marker =dict(
                color =['red','blue','green','yellow']
                     ),
                   )
data1 =[trace1]
plot(data1)