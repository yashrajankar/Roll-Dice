import random

while True:
    userInput = input("Roll a dice ? (y/n): ")
    if userInput.lower() == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif userInput.lower() == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input")