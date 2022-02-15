n=int(input('Enter height :- '))
#first approach
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
#second approach
for i in range(1,n+1):
    print("")
    for j in range(n,0,-1):
        if(i >= j):
            print("*",end="")
        else:
            print(end=" ")
    if i >= 2:
        for k in range(1,n):
            if(i > k ):
                print("*",end="")
