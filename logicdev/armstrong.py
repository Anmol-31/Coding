def armstrong(n):
    y = n
    x,z = 0,0
    while(y != 0):
        x += 1
        y //= 10
    y = n
    while(y != 0):
        z += (y%10)**x
        y //= 10
    return z

a = int(input("Enter The Number:- "))
b = armstrong(a)
if (a == b):
    print(f"{a} is a Armstrong Number")
else:
    print(f"{a} is not a Armstrong Number")
