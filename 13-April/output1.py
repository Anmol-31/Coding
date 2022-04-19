a=[i for i in range(10) if i%2]
a.extend(a)
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(len(b))
