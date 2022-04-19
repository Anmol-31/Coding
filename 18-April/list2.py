my_list = []
a = []
b = []
n1 = int(input("Enter number of elements of list:-"))
for i in range(n1):
    x = input("Enter the Input:-")
    my_list.append(x)
n = int(input("Enter the elements to be there in sublists:-"))
# for i in range(n1//n):
#     a.clear()
#     while(len(a) != n):
#         a.append(my_list[j])
#         j += 1
#     my_list.append(a.copy())
# a.clear()
# if n1 % n != 0:
#     for i in range(1,n1%n+1):
#         a.append(my_list[n1//n + i])
#     my_list.append(a.copy())
# # print(my_list)
# for i in range(n1):
#     my_list.pop(0)
#
# print(f"New List is {my_list}")
for i in range(n1):
    a.append(my_list[i])
    if len(a) == n:
        b.append(a)
        a = []
b.append(a)
print(b)
