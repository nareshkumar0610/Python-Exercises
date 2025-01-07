# Method 1:

# Take input from the user
S = input("Type the word: ")

# Reverse the string using slicing
rev_str = S[::-1]

# Print the reversed string
print(rev_str)



# Method 2:

# Take input from the user
s = input("Type the word: ")

# Initialize an empty string to store the reversed word
Rev_Str = ""

# Loop through the string in reverse order
for i in range(len(s)-1, -1, -1):
    # Append each character to the Rev_Str
    Rev_Str += s[i]

# Print the reversed string
print(Rev_Str)



