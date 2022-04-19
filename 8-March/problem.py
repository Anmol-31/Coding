a,b,c='','',{}
dict1 = {'a': {'b':{}},
               'c': {'d':{}},
               'e':{'f':{}}}
for i,j in dict1.items():
    for k in j:
        a = i
        b = k
        c[b] = {a:{}}
print(c)        
