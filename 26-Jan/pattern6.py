'''
* * * * * * * * * *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * *
'''


'''
* * * *
*     *
*     *
* * * *
'''
n = int(input("enter the size :- "))
for i in range(1,n+1):
    print("")
    if i == 1 or i == n:
        for j in range(1,2*n):
            if(j%2 != 0):
                print("*",end="")
            else:
                print(end=" ")
    else:
        for j in range(1,2*n):
            if(j == 1 or j == 2*n - 1):
                print("*",end="")
            else:
                print(" ",end="")
