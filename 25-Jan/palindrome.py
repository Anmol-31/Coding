def pd(n):
    x =0
    y=n
    while(y!=0):
        x = x*10 + y%10
        y //= 10
    return x

for i in range(1,100):
    if(pd(i) == i):
        print(i)
