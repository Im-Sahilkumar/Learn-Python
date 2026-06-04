# check is a string is a palindrome
userinput = input("enter a number")
print(userinput)
vowels = "aeiouAEIOU"
count = 0

for a in userinput:
    if a in vowels:
        print(a)
        count += 1
print("vowels count", count)

revstring=userinput[-1::-1]
print(revstring)

if revstring==userinput:
    print("yes")
else:
    print("no")