import random

def gameWin(computer, you):
    if computer == you:
        return None
    
    # Snake cases
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    
    # Water cases
    elif computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    
    # Gun cases
    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Welcome to Snake, Water, Gun Game!")
print("Type 'q' anytime to quit.\n")

while True:
    randNo = random.randint(1, 3)
    if randNo == 1:
        computer = 's'
    elif randNo == 2:
        computer = 'w'
    else:
        computer = 'g'

    you = input("Your Turn: Snake(s), Water(w), Gun(g)? ")

    if you.lower() == 'q':
        print("Thanks for playing! Goodbye g")
        break

    if you not in ['s', 'w', 'g']:
        print("Invalid choice! Please choose 's', 'w', or 'g'.\n")
        continue

    a = gameWin(computer, you)

    print(f"Computer chose {computer}")
    print(f"You chose {you}")

    if a is None:
        print("The game is a tie!\n")
    elif a:
        print("You win!\n")
    else:
        print("You lose!\n")
