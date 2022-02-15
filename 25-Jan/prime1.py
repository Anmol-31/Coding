def primeChecker(i):
    for j in range(2,i):
        if(i % j == 0):#checking prime or not
            break
            return ""
        if(i == j+1):
            return i

# print(2)
# for i in range(3,100+1):
#     x = 0
#     for j in range(2,(i+1)//2):
#         if i%j == 0:
#             x += 1
#     if x == 0:
#         # print(i)
print(2)
for i in range(3,100+1):
    print(primeChecker(i))
#     for j in range(2,i):
#         if(i % j == 0):#checking prime or not
#             break
#         if(i == j+1):
#             print(i)
