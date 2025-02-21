# a = int(input("Emter a number : "))

# if(a%2==0):
#     b= "even"
# else:
#     b= "odd"

# print("The number is : ",b)

# a = int(input("Emter 1st number : "))
# b = int(input("Emter 2nd number : "))
# c = int(input("Emter 3rd number : "))

# if((a>b)&(a>c)):
#     d=a
# elif((b>a)&(b>c)):
#     d=b
# else:
#     d=c
# print("The largest number is : ",d)

# a = int(input("Emter a number : "))

# if(a%7==0):
#     d= "yes"
# else:
#     d= "not"

# print(" the number multiply by 7 is ",d)

# a =[input("Enter the three movie name : ")]
# print(a)
# print(type(a))

# b= input("Enter 1st movie name :")
# c= input("Enter 2nd movie name :")
# d= input("Enter 3rd movie name :")

# e = []
# e.append(b)
# e.append(c)
# e.append(d)
# print(e)
# print(type(e))

# a = ["m","a","a","m"]
# b= a.copy()
# b.reverse()
# print("This is list a = ",a)
# print("this is list b = ",b)

# if (a==b):
#     print("list a is palindrom")
# else:
#     print("list a is not palindom")


# Grade = ("C","D","A","A","B","B","A")
# print(Grade.count("A"))

# Grade =["C","D","A","A","B","B","A"]
# print(type(Grade))
# Grade.sort()
# print(Grade)

# Dictionary = {
#     "table" : ["a piece of furnitur", "list of facts $ figure"],
#     "cat" : "a small animal"
# }
# print(Dictionary)

# subject = {"pythin","java","C++","pythin","javascript","java","pythin","java","C++","C"}
# print("Total number of class room are needed is : ",len(subject))

# Subject = {}

# a = int(input("Enter marks of phy : "))
# Subject.update({"physic" : a})
# a = int(input("Enter marks of che : "))
# Subject.update({"chemistry" : a})
# a = int(input("Enter marks of math : "))
# Subject.update({"math" : a})

# print(Subject)

# set = {9, "9.0", "8", 8.0}
# print(set)

# values = {
#     ("float", 9.0),
#     ("int", 9)
# }

# print(values)

# i = 1

# while i <= 99:
#     i += 1
#     print(i)

# a = int(input("Enter a number : \n"))

# i = a

# while i  <= 100:
#     i += a
#     print(i)

# a = int(input("Enter a number : \n"))

# num = [1,4,9,16,25,36,49,64,81,100]

# x = int(input("enter num = "))

# i = 0

# while i < len(num):
#     if (num[i] == x):
#         print( i)
#     else:
#         print()
#     i += 1
    
# list = [1,4,9,16,25,36,49,64,81,100]
# for val in list:
#     print(val)    

# tup = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("enter a number what you have found : "))
# for val in tup:
#     if (val == x):
#         print(x," is found")
#         break
#     print(val)

# n = int(input("Enter a number = " ))
# for i in range(1,11,1):
#     print(n,"*",i,"=",n*i)

# n = int(input("Enter the number : "))
# sum = 0
# i = 0
# while (i <= n):
#     sum += i
#     i += 1
# print("Total sum = ",sum)

# n = int(input("Enter the number : "))
# fac = 1
# i = 1
# while (i <= n):
#     fac *= i
#     i += 1
# print("Total fac of n = ",fac)

# n = int(input("Enter the number : "))
# fac = 1
# for i in range(1,n+1,1):
#     fac *= i
# print("the factorial of n number is : ",fac)

# num = [1,4,9,16,25,36,49,64,81,100]
# city = ["dhaka","chuadanga","darshona","khulna"]

# def list_len(a):
#     print(len(a))
#     return

# list_len(num)
# list_len(city)

# num = [1,4,9,16,25,36,49,64,81,100]
# city = ["dhaka","chuadanga","darshona","khulna"]

# def print_list(list):
#     for item in list:
        
#         print(item, end=" ")
        

# print_list(num)
# print()
# print_list(city)




# def factorial(a):
#     fac = 1
#     for i in range(1,a+1,1):
#         fac *= i
#     print("factorial of n = ", fac)
#     return


# n = int(input("Enter the number : "))
# factorial(n)




# def convater(USD):
#     BDT = 100
#     BDT *= USD
#     print("The BDT value is = ", BDT)
#     return

# a = int(input("Enter the USD : "))
# convater(a)

# def cheaker(a):
#     if (a%2==0):
#         print("Even")
#     else:
#         print("ODD")

# b = int(input("Enter a number : "))
# cheaker(b)


# def calculer_sum(n):
#     if (n == 0):
#         return 0
    
#     return calculer_sum(n-1)+n

# sum = calculer_sum(5)
# print(sum)

# list = [1,4,9,16,25,36,49,64,81,100]

# def value(list1, i=0):
#     if(i == len(list1)):
#         return 
#     print(list1[i])
#     value(list1, i+1)

# value(list)


# with open("practice.txt","w") as f:
#     f.write(" Hi everyone \n we are learning File I/O \n using Java \n i like programming in Java")

# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java", "python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.find("learning")
# if (new_data != -1):
#     print("Learning word is existing")
# else:
#     print("not found")
# print(new_data)

# with open("practice.txt","r") as f:
#     data = f.readline(2)

# new_data = data.find("learning")
# if (new_data != -1):
#     print("Learning word is existing")
# else:
#     print("not found")
# print(new_data)


# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#             line_no += 1
#     return -1

# check_for_line()




# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

#     count = 0
#     nums = data.split(",")
#     for val in nums:
#         if(int(val)%2 == 0):

#             count += 1

# print(count)

# print(__name__)