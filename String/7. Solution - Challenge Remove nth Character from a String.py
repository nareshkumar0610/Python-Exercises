
s = input("Type anything: ")
r = int(input("Type the number to remove the letter: "))
new_word = ""

for i in range(len(s)):
    if i != r:
        new_word += s[i]

print(new_word)






