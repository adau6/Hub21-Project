#String
"ada"
"hub21! coding"

#String manipulation
#We can think strings as a list of characters

#to go over each character of a string -> Use a for loop!
username = "pandamonaium1"
for char in username:
	print(char)

#we have index in strings as well:
print(username[5])

#concatenation: putting strings together, gluing them up
string1 = "coding is"
string2 = " fun"
string3 = " boring"

new_string = string1 + string2
print(new_string)

#lower/upper case
print(username.upper())
username = username.upper()
print(username)

username = username.lower()
print(username)

#check if it is lower case or upper case
a = "Aaaaa"
b = "bbbbb"
c = "CCCCC"
d = "DdDdDd"

print(a.islower()) # False
print(a.isupper()) # False
print(b.islower()) # True
print(b.isupper()) # False
print(c.islower()) # False
print(c.isupper()) # True
print(d.islower()) # False
print(d.isupper()) # False

#Challenge 1:
#You are given a name variable, you need make the first letter of the name capital and print hello, name
#Eg. Hello, Ada

name = "aDa"
#Step 1: Take the first letter
first = name[0]

#Step 2: Make the first letter upper case
first = first.upper()

#Step 3: Get the rest of the letters in name
#Remember the range: name[1:5] will give you letters from index 1 to 4, does not include 5
rest = name[1:len(name)]

#Step 4: Make the rest lower case in case there are some upper case letters
rest = rest.lower()

#Step 5: Concatenate the first letter and the rest of the letters
name = first + rest

#Step 6: The final step!! Print the Hello, Ada 
print("Hello,",name)

