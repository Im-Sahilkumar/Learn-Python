# check if a number is prime or not
num = eval(input("Enter a number: "))
primestat = True
midvalue = num//2
for n in range (2,midvalue):
    if num%n==0:
        primestat = False
        break
if primestat:
    print (num,"is a prime number")
else:
    print (num,"is not a prime number")