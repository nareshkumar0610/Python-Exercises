# Method 1:
# Get the letter based on index number

S = input("Type the word: ")
i = int(input("Type the number to get the letter: "))

if S == "":
    print("Empty String")
elif len(S) < i:
    print(f"{i} is out of range")
elif S != "":
    print(S[i])



# Method 2:
# # Get the number based on letter

s = input("Type the word: ")
i = input("Type the letter to get the index number: ")

if s == "":
    print("Empty String")
elif i not in s:
    print(f"letter {i} is not in the word {s}")
elif s != "":
    print(s.index(i))

