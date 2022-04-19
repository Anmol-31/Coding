dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5}

'''
First usage
'''

a = dict1.pop('a')#usage one
print(a)
print(dict1)

'''
Second Usage
'''
dict1.pop('f')
print(dict1)

'''
Third Usage
'''
d = dict1.pop('f','Not Available')
print(d)
print(dict1)
