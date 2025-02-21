# 1. Write a function called calculate_area 
#    that takes base and height as aninput 
#    and returns and area of a triangle.


def calculet_area(a,b):
    area = (1/2)*a*b
    return area

base = int(input("enter the base of triangle : "))
hight = int(input("Enter the hight of the triangle :"))

print("the area of the triangle is = ",calculet_area(base,hight))