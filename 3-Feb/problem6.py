def pd(n):
    x =0
    y=n
    while(y!=0):
        x = x*10 + y%10
        y //= 10
    return x
a = 0
b = 0
n = int(input("enter the number :- "))
for i in range(n,0,-1):
    if(i == pd(i)):
        a = i
        break
for i in range(n,2*n):
    if(i == pd(i)):
        b = i
        break
if n-a > b-n:
    print(b)
else:
    print(a)
#map padhganaa hai
