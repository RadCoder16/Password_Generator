# THis program gets the information from the user

#Variables

name = str(input("Enter your First Name: "))
last = str(input("Enter your Last Name: "))
email = input("Enter your email address: ")
password = input("Enter your password: ")
name_last = ("Hello {} {}".format(name, last))

#A list to check if there is symbols in the password

symbols = ["%, !, @, #, $, &, *, (, ), +, -, ?,"]
numbers = ["1234567890"]

#I need to find a way to add functions to make it more professional.
 

#Statements

if len(name) < 3:
    print("Error!. Length of name must be four characters or more.")
elif len(last) > 20:
    print("Length of name must not exceed twenty characters.")
if len(last) < 3:
    print("Error!. Length of name must be four characters or more.") 
elif len(last) > 20:
    print("Length of name must not exceed twenty characters.")
else:
    print(name_last)

if len(password) < 3:
    print("Weak!. Password must have numbers and not less than four characters.")
else:
    print("Strong Password!")

if password != symbols:
	print("Error!.Password must have symbols.")
else:
	print("rgfdgdgdg")

if password != numbers:
    print("Error!.Password must also have numbers")
else:
    print("Strong password!")

#Still a basic program but as time goes on I promise it will improve I promise
