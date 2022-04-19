'''
Item Method
'''
dict1 = {'Apple':1,'Microsoft':2,'Google':3}
print(dict1.items())
a =dict1.items()
print(a)
# for i,j in dict1:
#     print(i,j) --> error aati hai
for i,j in dict1.items():
    print(i,j) 
