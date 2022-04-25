def automorphic(n):
    y = n
    x = 0
    while(y != 0):
        x += 1
        y //= 10
    print(x)
    if n == (n*n)%10**x:
        return "Number is Automorphic"
    else:
        return "Number is Not Automorphic"

a = int(input("Enter number:- "))
print(automorphic(a))
