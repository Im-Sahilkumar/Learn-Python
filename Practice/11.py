# check if a number is a perfectnumber
num = eval(input("Enter a number: "))
total = 0
for n in range(1,num):
    if num%n==0:
        total = total + n
if total == num:
    print (num,"is a perfect number")
else:
    print (num,"is not a perfect number")