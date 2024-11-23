print("Welcome to Python Pizza Deliveries!")
S = 15
M = 20
L = 25
bill = 0
peporoni = 2
extra_cheese = 3
pizza_size = str(input("What Size Do You Want Your Pizza To be S, M , L : "))
peporoni = input("Do you want pepproni added to your pizza if yes type y and for no type n : ")
extra_cheese = input("Do you want Extra Cheese in your pizza y for yes and no for n : ")

if(pizza_size == 'S'):
    bill = 15
    print("Small Pizza $15")
    if(peporoni == 'y'):
        bill = bill + 2
        print("peproni added")
    else:(peporoni == 'n')
    bill = bill
    if(extra_cheese == 'y'):
            bill += 3
            print("extra cheese is added")
    else:(extra_cheese == 'n')
    bill = bill
    print(f"Your total bill is ${bill}")


if(pizza_size == 'M'):
    bill = 20
    print("Medium Pizza $20")
    if(peporoni == 'y'):
        bill = bill + 2
        print("peproni added")
    else:(peporoni == 'n')
    bill = bill
    if(extra_cheese == 'y'):
            bill += 3
            print("extra cheese is added")
    else:(extra_cheese == 'n')
    bill = bill
    print(f"Your total bill is ${bill}")



if(pizza_size == 'L'):
    bill = 25
    print("Large Pizza $25")
    if(peporoni == 'y'):
        bill = bill + 2
        print("peproni added")
    else:(peporoni == 'n')
    bill = bill
    if(extra_cheese == 'y'):
            bill += 3
            print("extra cheese is added")
    else:(extra_cheese == 'n')
    bill = bill
    print(f"Your total bill is ${bill}")