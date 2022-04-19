'''
Copy Method
'''
dict1 = {'Apple':1,'Microsoft':2}
dict2 = dict1
print(id(dict1),id(dict2))
dict3 = dict1.copy()
print(id(dict3))
