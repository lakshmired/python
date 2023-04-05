# 1)write a 4 functions
# a)to find the area of circle
# b) to find the area of rectangle
# c)to find the area of square
# d)find the area of triangle
# use return statements and print it 
# for taking the inputs use input()

import math

def area_of_the_circle (Radius):   
    area = Radius** 2 * math.pi  
    return area  
  
Radius = float (input ("Please enter the radius of the given circle: "))  
print (" The area of the given circle is: ", area_of_the_circle (Radius))  

def area_of_the_rectangle (l,b):
    area=l*b*math.pi
    return area
length=float(input("please enter the length of the rectangle"))
breadth=float(input("please enter the breadth of the rectangle"))

print ("the area of the given rectangle is:",area_of_the_rectangle(length,breadth)) 


def area_of_the_triangle (b,h):
    area=0.5*b*h*math.pi
    return area
base=int(input("please enter the base of the triangle"))
height=int(input("please enter the height of the triangle"))

print ("the area of the given triangle is:",area_of_the_triangle(base,height)) 


def area_of_the_square (s):
    area=s*s*math.pi
    return area

side=int(input("please enter the side of the square"))

print ("the area of the given square is:",area_of_the_square(side)) 

