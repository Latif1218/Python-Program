# 6. Write circle_calc() function that takes radius of a 
#    circle as an input from user and then it calculates 
#    and returns area, circumference and diameter. You 
#    should get these values in your main program by 
#    calling circle_calc function and then print them


def circle_calc(b):
    r = int(input("Enter the circle radiouc : "))
    if b == "area":
        area = 3.1416*(r*r)
        print("circle area = ",round(area,2))
    elif b == "circumference":
        circumference = 2*3.1416*r
        print("the circle circumference is = ",round(circumference,2))
    elif b == "diameter":
        diameter = 2*r
        print("rhe circle diameter is = ",round(diameter,2))
    else:
        print("option is not exist :")

a = input("what you need area, circumference, diameter :")
circle_calc(a)

