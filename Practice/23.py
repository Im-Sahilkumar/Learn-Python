#find the max and min in a list 
l = [20,35,55,67]
max = l[0]
for v in l:
    if v > max:
        max = v
print("max", max)
min = l[0]
for v in l:
    if v < min:
        min = v
print("min", min)   
