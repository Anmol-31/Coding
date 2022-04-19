def count1(x,y):
    z = 0
    for i in x:
        if i == y:
            z += 1
    return z
a = [1,1,2,5,5,8,2,8,"Anmol","Anmol"]
b ={}
for i in a:
    b[f"{i}"] = count1(a,i)
print(b)
