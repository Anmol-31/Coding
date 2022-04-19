def frequency(n):
    m,p = [],[]
    for i in n:
        for j in m:
            if i == j:
                break
        else:
            m.append(i)
    for i in m:
        x = 0
        for j in n:
            if i == j:
                x += 1
        p.append(f"{i} = {x}")
    return p    





n = int(input("Enter Number Of Elements Of List:- "))
a = list()
for i in range(n):
    x = input("Enter elements")
    a.append(x)
b = frequency(a)
print(b)
