dict1 = {'Apple':1,'Microsoft':2,'Google':3}
print(dict1)
print(type(dict1))
dict1['Instagram']=4 #for insertion of new key and value
print(dict1,id(dict1))
dict1['Apple'] = 10
print(dict1)
print(dict1['Microsoft'])
#print(dict1['Facebook']) ---> error ayega because exist niii krta dict1 mai

'''
 Keys
'''
# Keys can be any immutable data type
# tuple can also be keys but only if they contain strings,numbers,tuples
#  if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key
# You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend()
# Dictionary are set of key: value pairs, with the requirement that the keys are unique (within one dictionary)
# read loudly last poibt


'''
Biggest Question now:-

Are dict mutables?

Ans : Yes
1. we can make change in a dict.
2. as dictionary have same address before and after any change in it
'''


'''
Second Biggest Question
Are Dict. Ordered?
yes dict. are ordered as we can reach element of dict by its keys just like we can elements of list or tuple with index
yes dict are ordered but, they are not insertion ordered before 3.6, but after 3.6 they are insertion ordered 

'''
