
def ind(x,y):
    a = 0
    for i in x:
        a += 1
        if i == y:
            break
    return a-1




def r(y,b):
    x = []
    for i in range(len(y)):
        if i == b:
            pass
        else:
            x += [a[i]]
    return x



a = []
n = int(input("Enter Number Of Elements:- "))
for i in range(n):
    b = input(f"Enter {i} element:- ")
    a += [b]


x = []
while(n!=0):
    if n == 1:
        x += a
        break
    for i in range(1,n):
        if a[0] == a[i]:
            n -= 1
            a = r(a,ind(a,a[i]))
            break
    else:
        n -= 1
        x += [a[0]]
        a = r(a,ind(a,a[0]))

print(x)
