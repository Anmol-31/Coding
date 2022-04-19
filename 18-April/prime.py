print(2)
print(3)
for i in range(3,10**7):
    a = 0
    for j in range(1,i//2):
        if i%j == 0:
            a += 1
        else:
            pass
    if a == 1 and i % 2 != 0:
        print(i)
