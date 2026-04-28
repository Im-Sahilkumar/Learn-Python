# swap values of two variables and print before and after ?
x = 10
y = 50

# first way

print("x", x, "y", y)

x = x+y # 10+50=60
y = x-y # 60-50=10 
x = x-y # 60-10=50

print("x", x, "y", y)

# second way

print("x", x, "y", y)

x,y = y,x

print("x", x, "y", y)