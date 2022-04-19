
#sort Method
a = [1,2,3,4,4,4,4,2,2]

#First Usage
# print(f'Before Sorting :- {id(a)}')
# a.sort()
# print(a)
# print(f'After Sorting :- {id(a)}')
# print(a.sort())
# b=a.sort()
# print(b)
# print(a.sort)

#Second Usage
# a.sort(reverse=True)
# print(a)
# print(a.sort())
# b=a.sort()
# print(b)
# print(a.sort)

#third usage
b=['Anmol','Raanu','Vishu','Tanu','Aakrati']
def way(b):
    return b[1]
b.sort(key=way)
print(b)
