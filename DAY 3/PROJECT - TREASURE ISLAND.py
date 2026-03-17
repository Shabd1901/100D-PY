print("Welcome to the Tresure Island")
print("You mission is to find the treasure")

direction = input("Do you wanna go left or right?: ").lower()

if direction == "left":
    print("Good Decision. You may proceed")

    swdec = input('Would you choose to '
                    'swim or wait for the boat: ').lower()
    if swdec == "wait":
        print("Good Decision. You may proceed")
        print("3 doors suddenly appeared in front of you")
        print("Red, Yellow, Blue")

        doordec = input("Select one of the doors: ").lower()
        if doordec == "yellow":
            print("Congratulations. You've won the Jackpot!")
        else:
            print("Game Over!")

    else:
        print("You were eaten by a Shark. Get lost")

else:
    print("Game Over. You failed. Go Home")