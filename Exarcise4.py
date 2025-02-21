# 4. We have following information on countries and their 
#    population (population is in crores),

# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21

# i. Using above create a dictionary of countries and 
#    its population

countries = {
    "china" : 143,
    "india" : 136,
    "usa" : 32,
    "pakistan" : 21
}

print(countries)
print(type(countries))


# ii. Write a program that asks user for three type of inputs,
    
#     a.print: if user enter print then it should print all 
#       countries with their population in this format,
#       china==>143
#       india==>136
#       usa==>32
#       pakistan==>21

# b. add: if user input add then it should further ask 
#    for a country name to add. If country already exist 
#    in our dataset then it should print that it exist and 
#    do nothing. If it doesn't then it asks for population 
#    and add that new country/population in our dictionary 
#    and print it

    # c. remove: when user inputs remove it should ask for a 
    #    country to remove. If country exist in our dictionary 
    #    then remove it and print new dictionary using format 
    #    shown above in (a). Else print that country doesn't 
    #    exist!

    # d, query: on this again ask user for which country he
    #    or she wants to query. When user inputs that country 
    #    it will print population of that country.


def print_dic():
    a = list(countries.values())
    b = list(countries.keys())
    for i in range(len(b)):
        if(i == ","):
            pass
        else:
            print(b[i] , "==>" , a[i])
# print_dic()

def option(f):
        if (f == "print"):
            print_dic()
        
        elif (f == "add"):
            add = input("Enter a country for add:")
            if (add in countries):
                print("already exist")
            else:
                d = input("Enter the population :")
                countries[add] = d
                print_dic()
        elif (f == "remove"):
            remove = input("Enter a country for remove:")
            if (remove in countries):
                countries.pop(remove)
                print_dic()
            else:
                print("the country not exixt in the dic")
        elif (f == "query"):
            check_popul = input("enter the country :")
            if (check_popul in countries):
                value = countries.get(check_popul)
                print(check_popul,"population is :",value)
            else:
                print("country not exist")


g = input("enter what you need print, add, remove, query :")
option(g)



