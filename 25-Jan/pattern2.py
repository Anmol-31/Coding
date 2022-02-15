'''
*
**
***
****
*****
******
*******
********
'''
n = int(input("Enter Size Of Pattern : "))
for i in range(1,n+1):
    for j in range (1,n+1):
        if(i >= j):
            print("*",end="")
    print("")
