# Method 1:

S = input("Type the word: ")
rev_str = S[::-1]
print(rev_str)



# Method 2:
s = input("Type the word: ")
Rev_Str = ""

for i in range(len(s)-1, -1, -1):
    Rev_Str += s[i]

print(Rev_Str)



