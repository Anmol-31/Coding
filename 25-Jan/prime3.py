def primeChecker2(i):
    x = 0
    for j in range(2,i//2):
        if(i % j == 0):
            x += 1
    return x



def primeChecker1(i):
    for j in range(2,i):
        if(i % j == 0):
            return
        if(i == j+1):
            return True
print(2)
for i in range(3,100+1):
    if primeChecker2(i)==0:
        print(i)
