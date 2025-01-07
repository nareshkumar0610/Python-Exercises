# Method 1:

# Ask the user to input a word
S = input("Type the word to find the lenght of the word: ")
# Use the built-in len() function to get the length of the string and print it
print(len(S))


# Method 2:
# Ask the user to input a word
s = input("Type the word to find the lenght of the word: ")

# Initialize a counter variable to 0
count = 0

# Loop through each character in the string 's'
for i in s:
    # For each character, increment the count by 1
    count+=1

# After the loop finishes, print the final count (length of the string)
print(count)





