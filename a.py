def sockMerchant(n, ar):
    x = 0
    q = 1
    a = ar
    while(n !=0 or n != 1 ):
        if a[0] == a[q]:
            x += 0
            a.pop(0)
            a.remove(a[q])
            q += 1
            n -= 2
    print(x)

a = 9
b =[1,1,2,2,3,3,4.4,5]
sockMerchant(a,b)
