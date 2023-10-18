# Python program to conversion ASCII to string

# take list
l = [75, 110, 111, 119, 32, 80, 114, 111, 103, 114, 97, 109]

# printing list
print("List of ASCII value =", l)

# ASCII to string using naive method
string = ""
for num in l:
    string = string + chr(num)
  
# Printing string
print ("String:", str(string))
