# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

# done by Pramod
def a(n):
    if n==1:
        return 1
    else:
        return a(n-1) + n

print(a(3))