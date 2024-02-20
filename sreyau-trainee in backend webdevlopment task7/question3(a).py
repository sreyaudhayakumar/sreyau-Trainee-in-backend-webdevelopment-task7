# 3) print the following patterns:
# a)

# 0
# 0 0
# 0 0 0
# 0 0 0 0

n=4
for i in range(4):
    for j in range(i+1):
        print("0",end="")
    print()