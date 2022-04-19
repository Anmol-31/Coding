s = input("Enter the Input:-")
a = ""
b = 0
for i in range(len(s)):
    if s[i] == " " or i == len(s)-1:
        if s[b:i] in a:
            pass
            b = i
        else:
            a += s[b:i]
            b = i
print(a)
