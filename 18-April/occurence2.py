def frequency(n):
    m = set(n)
    p = []    
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
