# check if a year is a leap year or not
num = eval(input("Enter a year: "))
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print(num, "is a leap year.")
else:
    print(num, "is not a leap year.")