a=[1,2,2,4,55,5,5,6,6,6,7,7,71,1,1]
b=[]
for i in a:
    if i not in b:
        b+=[i]

print(b)
