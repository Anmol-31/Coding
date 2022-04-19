n = [1,2,3,4,5]
a = []
b = 0
for i in n:
    b += 1
while(b != 0):
    a += [n[b-1]]
    b -= 1
print(a)
