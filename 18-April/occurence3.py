def frequency(n):
    a = dict.fromkeys(n,0)
    for i in a:
        for j in n:
            if i == j:
                a.update({i:a[i]+1})
    return a
l = int(input())
a = list()

for i in range(l):
    a.append(input())
for i in range(l):
    a[i] = int(a[i])



b = frequency(a)
print(b)
