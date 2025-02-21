# 3. Write a function called print_pattern that 
#    takes integer number as an argument and prints 
#    following pattern if input number is 3,



def  triangle_pattern(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print("*", end = "    ")
        print("\n")

a = int(input("Enter the number : "))
triangle_pattern(a)
