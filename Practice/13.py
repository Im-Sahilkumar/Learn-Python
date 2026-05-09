# reverse a number using while loop
num = eval(input("Enter a number: "))
reverse = 0
while num>0:
    lastdigit = num%10
    reverse = reverse*10 + lastdigit
    num = num//10
print("The reverse of the number is:", reverse)
