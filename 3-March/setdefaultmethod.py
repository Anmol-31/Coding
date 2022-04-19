dict1 ={'a':1,'b':2,'c':3,'d':4}

#First usage

x = dict1.setdefault('b')
print(dict1)
print(x)

#Second usage

y = dict1.setdefault('e')
print(y)
print(dict1)


#Third usage

z = dict1.setdefault('f','Added a New Key')
print(z)
print(dict1)
