z= []
a = []
n1 = int(input("Enter number of elements of list:-"))
for i in range(n1):
    x = input("Enter the Input:-")
    z.append(x)
n = int(input("Enter the elements to be there in sublists:-"))


a=[z[i:i+n] for i in range(0,len(z),n)]
print(a)


# [1,5,6,7,2,7,9,3,8]
# dry run krna hai,push all to github
