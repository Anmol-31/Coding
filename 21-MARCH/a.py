# class stack:
#     def __init__(self)
#         self.items = []
#     def isempty(self):
#         return self.items == []
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         self.items.pop()
#     def top(self):
#         return len(items)-1
#     def size1(self):
#         return len(items)
#
#
#
#
x = [9,8,7,4,6,9,2,3,99,74]
# for i in range(len(x)-1):
#     for j in range(len(x)-1):
#         if x[j+1] <= x[j]:
#             t = x[j]                  #Bubble sort
#             x[j] = x[j+1]
#             x[j+1] = t
#         else:
#             continue
# for i in range(len(x)):
#     t = x[i]
#     for j in range(i,len(x)):
#         if t > x[j]:
#             t = x[j]
#             p = j
#     x[p] = x[i]
#     x[i] = t
for i in range(1,len(x)):
    value = x[i]
    hole = i
    while(hole >0 and x[hole-1] > value):
        x[hole] = x[hole-1]
        hole = hole - 1
    x[hole] = value


print(x)
