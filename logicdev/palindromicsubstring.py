def palindrome(n):
    if n[0] == n[-1]:
        if len(n) == 1 or len(n) == 2:
            return 1
        else:
            return palindrome(n[1:-1])
    else:
        return 0


def substring(n,y,a = 0):
    if a != len(n)-y+1:
        if palindrome(n[a:y+a]) == 1:
            print(n[a:y+a],end=" ")
            return substring(n,y,a+1)
        else:
            return substring(n,y,a+1)
    else:
        return

n = input("Enter Input String:-")
for i in range(1,len(n)+1):
    substring(n,i)
