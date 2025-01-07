
s = input("Type Anything: ")
ns = ""

for i in range(len(s)):
    if len(s) < 2:
        print(s)

    elif i % 2 != 0:
        ns += s[i]

print(ns)


