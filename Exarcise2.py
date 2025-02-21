# 2. Modify above function to take third parameter 
#    shape type. It can be either "triangle" or "rectangle". 
#    Based on shape type it will calculate area. 

def calculate_area(a,b,c):
    if (c == "triangle"):
        area = (1/2)*a*b
    elif (c == "rectangle"):
        area = a * b
    else:
        print("not detarmind")

    return area

base = int(input("enter the bas of triangle :"))
hight = int(input("enter the hight of triangle :"))
print("thr area of triangle = ",calculate_area(base,hight,"triangle"))


length = int(input("enter the length of rectangle :")) 
width = int(input("enter the width of rectangle :")) 
print("thr area of rectangle = ",calculate_area(length,width,"rectangle"))