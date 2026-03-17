print("Welcome to Pizza Deliveries!")
size =  input("What size do you want for your pizza? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese = input("Do you want extra cheese? y or n: ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid reponse")

if pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}")