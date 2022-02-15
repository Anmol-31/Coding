'''
@
##
@@@
####
@@@@@
'''
n = int(input("Enter Height of Pattern :- "))
for i in range (1,n+1):
    if(i%2 != 0):
        for j in range(1,n+1):
            if(i >= j):
                print("@",end="")
    else:
        for j in range(1,n+1):
            if(i >= j):
                print("#",end="")
    print("")
