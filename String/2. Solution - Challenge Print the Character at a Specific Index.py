# Method 1:

# Take a string input from the user
S = input("Type the word: ")

# Take an integer input as the index
i = int(input("Type the number to get the letter: "))

# Check if the string is empty
if S == "":
    print("Empty String")   # If the string is empty, print an error message

# Check if the index is out of range
elif len(S) < i:
    print(f"{i} is out of range")   # If the index is not valid, print an error message

# If the string is not empty and the index is valid
elif S != "":
    print(S[i])     # Print the character at the specified index



# Method 2:

# Take a string input from the user
s = input("Type the word: ")

# Take an integer input as the index
i = input("Type the letter to get the index number: ")

# Check if the string is empty
if s == "":
    print("Empty String")       # If the string is empty, print an error message

# Check if the index is out of range
elif i not in s:
    print(f"letter {i} is not in the word {s}")     # If the index is not valid, print an error message

# If the string is not empty and the index is valid
elif s != "":
    print(s.index(i))       # Print the character at the specified index



