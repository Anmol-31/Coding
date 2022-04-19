# x =[]
# for i in range(1,5):
#     for j in range (5,0,-1):
#         x.append(i*j)
# print(x)

# b = [i*j for i in range(1,5) for j in range(5,0,-1) ]
# print(b)


# a = []
# for i in range(5):
#     a.append(i)
# print(a)


# d = [i for i in range(5)]
# print(d)

a = []
for i in range(10):
    if i%2 == 0:
        a.append(i)
print(a)



b = [i for i in range(10) if i%2 == 0]
print(b)
