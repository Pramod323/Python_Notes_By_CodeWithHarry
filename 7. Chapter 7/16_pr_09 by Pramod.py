n = 3

for i in range(1,4):
    if i%2 == 0:
        print("*"*(n-2) + " "*(n-2) + "*"*(n-2))
        continue
    elif i%2 != 0:
        print("*"*n)