import random


response = "y"


while response == "y":
    
    number = random.randint(1, 6)

    # print the dice output
    print("-------")
    
    if number == 1:
        print("|   |")
        print("| 0 |")
        print("|   |")
    elif number == 2:
        print("|0  |")
        print("|   |")
        print("|  0|")
    elif number == 3:
        print("|   |")
        print("|000|")
        print("|   |")
    elif number == 4:
        print("|0 0|")
        print("|   |")
        print("|0 0|")
    elif number == 5:
        print("|0 0|")
        print("| 0 |")
        print("|0 0|")
    elif number == 6:
        print("|0 0|")
        print("|0 0|")
        print("|0 0|")

    
    print("-------")

    response = input("Do you want to roll again? (y/n): ").lower()

    # check if the user entered a valid response
    if response != "y" and response != "n":
        response = input("Invalid response. Do you want to roll again? (y/n): ").lower()

# print a message when the loop ends
print("Thanks for playing!")
