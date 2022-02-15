for i in range (1,10**6 + 1):
    a =0
    b = i
    while(b > 0):
        a += (b%10)**3
        b //= 10
    if(i == a):
        print(i)
    else:
        pass
