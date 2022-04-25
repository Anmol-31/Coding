def prod(x1,y1,n1,z1 = []):
    p = []
    for i in range(n):
        for j in range(n):
            l = 0
            for k in range(n):
                l += x1[i][k]*y1[k][j]
            z1.append(l)
        p.append(z1)
        z1 = []
    print(x1,y1,p,end="\n")





n = int(input("Enter n of nXn matrices"))
x,y = [],[]
z = []
sum = []
print("Enter element of X")
for i in range(n):
    for j in range(n):
        z.append(int(input("")))
    x.append(z)
    z = []
print("Enter element of Y")
for i in range(n):
    for j in range(n):
        z.append(int(input("")))
    y.append(z)
    z = []
prod(x,y)
