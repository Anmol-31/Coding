def Amn(n):
    y = 0
    a = n
    while(a != 0):
        y += 1
        a //= 10
    if n == (n*n)%(10**y):
        return True
    else:
        return False
n = int(input("Enter The Number"))
print(Amn(n))
