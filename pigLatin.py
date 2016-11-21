"""
Pig Latin: Move the first letter of the word to the end and add "ay"; Python >> ythopay
"""

print('Welcome to the Pig Latin Translator!')

original = input("What would you like to translate? \n")

## Check if the user's string has characters, and characters are alphabets
if len(original) > 0 and original.isalpha() == True:
    print("Your word is " + original)
else:
    print("No characters to translate.")

## Letter conversion
pyg = "ay"

word = original.lower()

first = original[0]

new_word = word[1:len(word)] + first.lower() + pyg

print("Pig Latin of " + original + " is " + new_word)