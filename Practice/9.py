# menu driven calculator (using if-elif-else statement)
print("Welcome to the menu driven calculator!")
print(  '''
      + add
      - subtract
      * multiply
      / divide
      ''')
num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
operation = input("Enter the operation you want to perform: ")
if operation == '+':
    result = num1 + num2
    print("The result is:", result)
elif operation == '-':
    result = num1 - num2
    print("The result is:", result)
elif operation == '*':
    result = num1 * num2
    print("The result is:", result)
elif operation == '/':
    result = num1 / num2
    print("The result is:", result)
else:
    print("Invalid operation. Please choose from +, -, *, /.")