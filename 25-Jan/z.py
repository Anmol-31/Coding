n =int(input("Enter Size :- "))
for i in range(1,n+1):
    if(i == 1 or i == n):
        for j in range(1,n+1):
            print("*",end="")
    else:
        for j in range(1,n):
            if(j == n - (i-1)):
                print("*",end = "")
            else:
                print(" ",end = "")
    print("")
