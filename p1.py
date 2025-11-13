# ask user for name
name = input("what is your full name? ")

# capitalize and Remove white spaces from the string 'name'
name = name.title().strip()

# to split first and last name
first, last = name.split(" ")

# say hello to user
print("hello, ", first)
print("first name - ", first)
print("last name - ", last)

# asking for age
age =int(input("what is your age? "))
age18=18

if age<age18:
    print ("go watch kochutv")
else:
    print ("come watch some porn ")

