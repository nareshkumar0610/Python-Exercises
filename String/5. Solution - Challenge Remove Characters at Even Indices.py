# Take input from the user
s = input("Type Anything: ")
# Initialize an empty string to store the new word in ns variable
ns = ""

# Loop through the lenght of the string
for i in range(len(s)):
    # Check if the lenght of the string is less than 2
    if len(s) < 2:
        # If True print string "s"
        print(s)

    # Else check for odd values using modulus operator
    elif i % 2 != 0:
        # Append each character to the ns variable
        ns += s[i]

# Print the output
print(ns)


