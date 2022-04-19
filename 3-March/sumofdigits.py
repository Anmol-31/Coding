def sod(n):
    if n == 0:
        return a
    else:
        a += n %  10
        n //= 10
        return sod(n,a)

n = int(input("enter user input :- "))
print(sod(n))
