n = 3
for i in range(3): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))




'''
n = (int(input("Enter your number?\n")))*2
numberList = []
for i in range(1, n+1):
    numberList.append(i)

numberList.reverse()

for i in range(n+1):
    if i%2 == 0:
        continue
    print(" "*int((numberList[i])/2) + "*"*i + " "*int((numberList[i])/2))



tried by Pramod, WHJR
'''