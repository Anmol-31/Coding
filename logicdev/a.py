n = int(input("Enter height greater or equal to 4:-"))
for i in range(n):
    if i == 2:
        print(" "*(n-3) + "*"*5)
    elif(i == 0):
        print(" "*(n-1) + "*")
    else:
        print(" "*(n-i-1)+ "*" +  " "*(2*i -1) + "*")
