steps = int(input("Enter number Steps:-"))
spath = input("Enter string Path:-")
a = 0
b =0
for i in spath:
    if a == 0:
        if i == 'D':
            a -= 1
            b += 1
    else:
        if i == 'D':
            a -= 1
        if i == 'U':
            a += 1

print(b)
