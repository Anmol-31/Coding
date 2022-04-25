n = int(input("Enter height greater than egual to 3:- "))
for i in range(n):
    if i == 0 or i == n-1:
        print("*"*n)
    else:
        print("*")    
