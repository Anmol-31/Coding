a = [1,2,3] # a can be any iterable
dict1 = dict.fromkeys(a)#1st usage
print(dict1)

b='Anmol'
dict2 = dict.fromkeys(a,b)#2nd usage
print(dict2)

c = [1]
dict3 = dict.fromkeys(a,c)#3rd usage
print(dict3)
c.append(2)
print(dict3)
