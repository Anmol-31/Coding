# a =[1,2,3,4,4,4,4,2,2]
# b = a.copy()
# print(b)
a =[1,2,3,4,5]
a += [6,7]
print(id(a))
print(a)

b =a.copy()
print(id(b))
print(b)

c = a
print(id(c))
print(c)

c+=[10,11]
print(id(a))
print(a)
