import random 

"""We are assigning some values to the element of this game
Snake : 1
Water : -1
Gun : 0
"""

computer = random.choice([0,-1,1])
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w" : -1, "g" : 0}
reversedict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = youdict[youstr]

print(f"You chose {reversedict[you]} and computer chose {reversedict[computer]}")


if computer == you:
    print("Its a draw")
else:
    if computer == 1 and you == -1:
        print("You lose")
    if computer == 1 and you == 0:
        print("You win")
    if computer == -1 and you == 1:
        print("You win")
    if computer == -1 and you == 0:
        print("You lose")
    if computer == 0  and you == 1:
        print("You lose")
    if computer == 0 and you == -1:
        print("You win")
    else:
        print("Something went wrong")

    
