x = int(input("Enter Value of x:-"))
y = int(input("Enter Value of y:-"))
grid = []
for i in range(y):
    grid.append([])

if y % 2 != 0:
    a = [0,1,((y-1)/2),y-1,y-2]
    for i,j in enumerate(grid):
        if i in a:
            j.append(".")
        else:
            j.append("0")

    for i,j in enumerate(grid):
        if i == 0 or i == y-1:
            j.append('.')
        else:
            j.append('0')

    for i in range(x-2):
        for k,j in enumerate(grid):
            if i >= k or k >= y-1-i:
                j.append('.')
            else:
                j.append('0')

for i in range(y):
    if i == x:
        break
    for k in grid:
        print(k[i],end = '')
    print(end="\n")    
