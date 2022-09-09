"""EX02 - One Shot Wordle - Another step toward Wordle."""

__author__ = "730622383"

secret_variable: str = "python"
secret_length: int = len(secret_variable)
# initializes the secret word and establishes its length

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

player_guess: str = input(f"What is your {secret_length}-letter guess?")
while len(player_guess) != secret_length:
    player_guess = input(f"That was not {secret_length} letters! Try again:")
    # takes a player guess and ensures its the same length as the secret word, while also providing the length in the printed statements

i: int = 0
emoji_guess_result: str = ""
while i < secret_length:
    j: int = 0
    if player_guess[i] == secret_variable[i]:
        emoji_guess_result = emoji_guess_result + GREEN_BOX
        # checks if the letter at the index is the same as in the secret word
    else:
        while j < secret_length:
            # itterates over the secret word again, checking to see if the letter at index j is at all present not just in the correct spot, if so, prints yellow, otherwise prints white
            if player_guess[i] == secret_variable[j]:
                emoji_guess_result = emoji_guess_result + YELLOW_BOX
                break
            j += 1
            if j == secret_length:
                emoji_guess_result = emoji_guess_result + WHITE_BOX
                break
    i += 1
print(emoji_guess_result)
if player_guess == secret_variable:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
# prints the green white yellow boxes, and the congratulations or tells of the loss