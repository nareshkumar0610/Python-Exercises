
s = input("Type anything: ")

if len(s) < 6:
    print("")
else:
    out = s[0:3] + s[-3:]
    print(out)

