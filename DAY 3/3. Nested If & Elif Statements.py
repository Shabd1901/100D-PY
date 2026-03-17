print("Welcome to the Roller Coaster")
height = int(input("Enter your height(in cm): "))
if height > 120:
    print("You can ride the Roller Coaster")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Please pay $12")
    elif age >=12:
        print("Please pay $7")
    else:
        print ("Please pay %5")
else:
    print("Sorry you need to grow taller before you can ride.")