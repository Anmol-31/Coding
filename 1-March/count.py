lst = []
n = int(input("Enter Total Number of element:- "))
a = 0
for i in range(n):
    a = int(input(f"Enter {n} Element of list:- "))
    lst.append(a)
x = int(input("enter number to be counted:- "))
a = 0
for i in lst:
    if i == x:
        a += 1
print(f"{x} appeared {a} times in a list")
