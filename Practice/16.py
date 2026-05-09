# invert stars output
# *****
# ****
# ***
# **
# *

for r in range(6,1,-1):
    for c in range(1, r):
        print("*", end="")
    print()

    # 2nd method
# for r in range(5, 0, -1):
#     print("*"*r)