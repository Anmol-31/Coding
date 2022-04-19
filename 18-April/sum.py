# def sum1(n,m = 0):
#     if n == 1:
#         return (m+1)
#     else:
#         return sum1(n-1,m + n)
a = 0
def sum2(n):
    global a
    if n == 1:
        return (a+1)
    else:
        a = a + n
        return sum2(n-1)
print(sum2(10))
