# Take input from the user
s = input("Type anything: ")

# Ask user to enter number for removing letter
r = int(input("Type the number to remove the letter: "))

# Initialize an empty string to store the new_word
new_word = ""

# Iterate through each character in the string 's'.
for i in range(len(s)):
    # If the current index 'i' is not equal to 'r' (the index to be removed),
    if i != r:
        new_word += s[i]    # Append the character at index 'i' to 'new_word'.

# Print the new word after the removal
print(new_word)






