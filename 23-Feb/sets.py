'''
A set is an unordered collection with no duplicate elements.
{}

'''
a =[9,1,2,3,3,4,4,4]
b = set(a)
for i in b:
    print(i)

print(b)
c = {1,2,3,5,5,4,4,9,1,2,9,3}
print(c)#no sorting in case of string but sorting in case of int
d = {2,2}
print(d)
e = {}
print(e)
print(type(e))
f = set()
print(f,type(f),sep ="\n")
g =set('anmolupadhyay')
print(g)
h = {"anmolupadhyay"}# special case
print(type(h))
print(type({"anmolupadhyay"}))
i =set("aakriti")
j = set("ankush")
print(i-j)#difference
print(i&j)#intersection
print(i|j)# union
print(i^j)#letter in a or b but not both
