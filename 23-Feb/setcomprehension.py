# a =[]
# for i in range(3):
#     for j in range(3):
#         a.append(i*j)
# print(a)
# b = [i*j for i in range(3) for j in range(3)]
# print(b)
#
#

a = set()
for i in range(3):
    for j in range(3):
        a.add(i*j)
print(a)
b = {i*j for i in range(3) for j in range(3)}
print(b)
