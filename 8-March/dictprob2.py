a =[1,1,2,5,5,8,2,8]
b = {}
for i in a:
    b[i]=b.get(i,0)+1
print(b)    
