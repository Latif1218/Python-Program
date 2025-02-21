# 5. You are given following list of stocks and 
#    their prices in last 3 days,

#    Stock	Prices
#    info	    [600,630,620]
#    ril	    [1430,1490,1567]
#    mtl	    [234,180,160]

# i. Write a program that asks user for operation. 
#    Value of operations could be,
#    a. print: When user enters print it should 
#       print following,

        # info ==> [600, 630, 620] ==> avg:  616.67
        # ril ==> [1430, 1490, 1567] ==> avg:  1495.67
        # mtl ==> [234, 180, 160] ==> avg:  191.33

    # b. add: When user enters 'add', it asks for stock 
    #    ticker and price. If stock already exist in your 
    #    list (like info, ril etc) then it will append 
    #    the price to the list. Otherwise it will create 
    #    new entry in your dictionary. For example entering 
    #    'tata' and 560 will add tata ==> [560] to the 
    #    dictionary of stocks.


import statistics
stocks = {
    "info" :    [600,630,620],
    "ril"  :	[1430,1490,1567],
    "mtl"  :	[234,180,160]
}

def print_all():
    for stock, price_list in stocks.items():
        avg = statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg: ",round(avg,2))

def add_all():
    add = input("Enter a atock ticker for add:")
    price = float(input("Enter the price :"))
    if (add in stocks):
        stocks[add].append(price)
    else:
        stocks[add] = [price]
    print_all()

def main():
    op = input("enter what do you need. print or add :")
    if op == "print":
        print_all()
    elif op == "add":
        add_all()
    else:
        print("not in option")

if __name__ == "__main__":
    main()