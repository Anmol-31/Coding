n = int(input("Enter half height greater or equal to 3:-"))
for i in range(2*n):
    if i == 0 or i == 2*n-1 or i == n-1 or i == n+1 :
        print("*"*n)
    elif(i == n):
        print("*")
    else:
        print("*" + " "*(n-2) + "*")
