# adharcard 16-digit validation (using string conditions only)

userinput=input("Enter your 16-digit adharcard number: ")
if userinput.isdigit() and len(userinput)==16:
    print("Valid adharcard number")
else:
    print("Invalid adharcard number")