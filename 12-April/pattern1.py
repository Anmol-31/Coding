n = int(input("Enter height:-"))
for i in range(n):
    for j in range(n):
        if i <= j:
            print("*",end= "")
    print()
