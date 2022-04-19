'''
Getmethod...
'''
dict1 = {'Apple':1,'Microsoft':2,'Google':3,'Instagram':4,'Facebook':5}
#First usage :
a = dict1.get('Google')
print(a)
b = dict1.get('Snapchat')# output comes out to be none
print(b)

#Second usage
c = dict1.get('Snapchat','not available')
print(c)
# by default if given key is not available in dict then it prints None
#but in case we give a second argument it prints that instead of None
