def kaprekar(n):
    x = n*n
    z = x
    y,p = 0,0
    while(z != 0):
        y += 1
        z //= 10
    if y == 1:
        p = x
    elif (y % 2 == 0):
        p = (x%10**(y//2)) + (x//10**(y//2))
    else:
        p = (x%10**(y//2 + 1)) + (x//10**(y//2+1))
    return p    

a = int(input("Enter The Number:- "))
k = kaprekar(a)
if (a == k):
    print(f"{a} is a Kaprekar Number")
else:
    print(f"{a} is not a Kaprekar Number")
