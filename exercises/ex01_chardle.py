"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730622383"

input_word: str = input("Enter a 5-character word: ")
if len(input_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_char: str = input("Enter a single character: ")
if len(single_char) != 1:
    print("Error: Character must be a single character.")
    exit()
instances_char_in_word: int = 0
print("Searching for", single_char, "in", input_word)

if input_word[0] == single_char:
    print(single_char, "found at index 0")
    instances_char_in_word = instances_char_in_word + 1
if input_word[1] == single_char:
    print(single_char, "found at index 1")
    instances_char_in_word = instances_char_in_word + 1
if input_word[2] == single_char:
    print(single_char, "found at index 2")
    instances_char_in_word = instances_char_in_word + 1
if input_word[3] == single_char:
    print(single_char, "found at index 3")
    instances_char_in_word = instances_char_in_word + 1
if input_word[4] == single_char:
    print(single_char, "found at index 4")
    instances_char_in_word = instances_char_in_word + 1

if instances_char_in_word == 1:
    print(instances_char_in_word, "instance of", single_char, "found in", input_word)
elif instances_char_in_word > 1:
    print(instances_char_in_word, "instances of", single_char, "found in", input_word)
else:
    print("No instances of", single_char, "found in", input_word)