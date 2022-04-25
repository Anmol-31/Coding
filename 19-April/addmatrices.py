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

for i in range(n):
    for j in range(n):
        z.append(x[i][j] +y[i][j])
    sum.append(z)
    z = []
print(x,y,sum,end="\n")    
