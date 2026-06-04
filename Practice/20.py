#count vowels in a string
userinput = input("enter a number")
print(userinput)
vowels = "aeiouAEIOU"
count = 0

for a in userinput:
    if a in vowels:
        print(a)
        count += 1
print("vowels count", count)