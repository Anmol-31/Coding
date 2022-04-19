def list1(x):
    y = []
    z = 0
    for i in range(len(x)):
        if x[i] == " ":
            y.append(x[z:i])
            z = i
    y.append(x[-1])
    return y


n = input("Enter Input:- ")
b = list1(n)
# for i in range(len(b)):
#     b[i] = int(b[i])
print(b)
