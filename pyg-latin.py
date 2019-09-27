"""
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." 
So "Python" becomes "ythonpay."
We will be asking the user for their input and then print the new word.
"""

# Lets create the pyg variable with “ay” as its value 
pyg = "ay"
def get_word():
    # Get user's input (word)
    original = input("Enter a word:")
    if len(original) > 0 and original.isalpha():
        # Check that the input is not empty and is made up of alphabetical characters.
        word = original.lower()
        first_letter = word[0]
        new_word = word[1:len(word)] + first_letter + pyg
        print(new_word)
    else:
        # If the input is invalid, ask the user again until they submit the right input.
        print("'%s' -- is not a valid word.\nTry again..." % (original))
        return get_word()

get_word()
