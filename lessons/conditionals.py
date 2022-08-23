"""An example of conditional (if-else) statements"""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))
if guess == SECRET:
    print("You got it!!!")
else:
    print("Not my number.")

print("Game over.")