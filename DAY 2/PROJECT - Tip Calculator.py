print("Welcome to TIP CALCULATOR!")

bill = float(input("Enter the total bill amount: "))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
no_of_people = int(input("How many people to split the bill? "))

total_bill = bill + ((bill * tip_percentage)/100)
split = round(total_bill / no_of_people, 3)

print(f"Each person should pay ${split}")           #--> fstring is used to avoid concatenation error
