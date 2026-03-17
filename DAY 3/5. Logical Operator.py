print("Welcome to the Roller Coaster")
height = int(input("Enter your height(in cm): "))
bill = 0

if height > 120:
    print("You can ride the Roller Coaster")
    age = int(input("Enter your age: "))
    if age >= 18:
        bill = 12
        print("Please pay $12")
    elif age >=12:
        bill = 7
        print("Please pay $7")
    elif age >=45 and age <=55: #--> representing AND operator. Could be written as "elif 45 >= age >= 55:"
        bill = 0
        print("Everything is going to be alright, you can ride for free.")
    else:
        bill = 5
        print ("Please pay %5")

    wants_photo = input("Do you want a photo for additional $3? Type y for Yes and n for No: ")
    if wants_photo == "y":
        bill = bill + 3  # bill += 3
        print("Your Final bill is ${bill}")
    elif wants_photo == "n":
        print("Your Final bill is ${bill}")
    else:
        print("Enter a valid response.")

else:
    print("Sorry you need to grow taller before you can ride.")