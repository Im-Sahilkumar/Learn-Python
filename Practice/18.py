# PAN card no validation (using string conditions only)

# no must be exactly 10 characters long

# the first 5 characters must be uppercase letters

# the next 4 characters must be digits(0-9)

# the last character must be an uppercase letter

userinput=input("Enter your PAN card number: ")
pannumber=userinput.upper()

if len(pannumber)==10 and pannumber[0:5].isalpha() and pannumber[0:5].isupper() and pannumber[5:9].isdigit() and pannumber[9].isalpha() and pannumber[9].isupper():
    print("Valid PAN card number")
else:
    print("Invalid PAN card number")