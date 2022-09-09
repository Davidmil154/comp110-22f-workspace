"""EX03 - Wordle - Terminal version of Wordle."""

__author__ = "730622383"

def contains_char(test_word: str, s_char: str) -> bool:
    """Checks that a character is in the test word."""
    assert len(s_char) == 1
    i: int = 0
    while i < len(test_word):
        if s_char[0] == test_word[i]:
            return(True)
        i += 1
        if i == len(test_word):
            return(False)

def emojified(player_guess: str, secret_word: str) -> str:
    """Takes a player guess, and returns the emjoified version, with green white and yellow boxes. Uses contains_char to check for white and yellow."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    return_word: str = ""
    j: int = 0
    while j < len(secret_word):
        if player_guess[j] == secret_word[j]:
            return_word += GREEN_BOX
        elif contains_char(secret_word, player_guess[j]) == True:
             return_word += YELLOW_BOX
        else:
             return_word += WHITE_BOX
        j += 1
    return(return_word)

def input_guess(secret_len: int) -> str:
    """Take input for a guess and returns it."""
    player_guess: str = input(f"Enter a {secret_len} character word:")
    while len(player_guess) != secret_len:
        player_guess = input(f"That wasn't {secret_len} chars! Try again:")
    return(player_guess)

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    secret_length: int = len(secret_word)
    turn: int = 1
    player_guess: str = ""
    while turn <= 6:
        # Main body of the program, where it runs through the players 6 turns. Passes out the emojified version, and if the player wins or loses
        print(f"=== {turn}/6 ===")
        player_guess = input_guess(secret_length)
        print(emojified(player_guess, secret_word))
        if player_guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            return()
        elif turn == 6:
            print(f"X/6 - Sorry, try again tomorrow!")
            return()
        turn += 1

if __name__ == "__main__":
    main()