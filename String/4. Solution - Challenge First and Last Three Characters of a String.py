# Take input from the user
s = input("Type anything: ")

# Check if the lenght of the string is less than 6
if len(s) < 6:
    print("")       #Is True print empty string
else:
    #Concatenate string "s" using slicing method
    out = s[0:3] + s[-3:]
    print(out)      #Print the out string




