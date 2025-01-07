# Take input from the user
s = input("Enter anything: ")

# Ask user to enter the character they wish to replace.
curr_char = input("Enter the character which you want to replace: ")

# Ask user to enter the new character that will replace the current character.
new_Char = input("Enter the new character you want to add: ")

# The replace() method creates a new string where all instances of 'curr_char' are replaced with 'new_Char'.
new_word = s.replace(curr_char, new_Char)

# Outputs the result showing the replacement.
print(f"You replaced the character '{curr_char}' with '{new_Char}' and the new word is '{new_word}'.")


