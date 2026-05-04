# Nested if 
print ('''
       + add
       - subtract
       * multiply
       / divide
''')

num1 = eval(input("enter first number: "))
num2 = eval(input("enter second number: "))
operator = input("enter operator: ")

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("invalid operator")    