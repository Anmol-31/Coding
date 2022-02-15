# def LcmHcf(n,m):
#     x = 1
#     for i in range(1,n*m):
#         if(n%i == 0 and m%i == 0):
#             if(i > x):
#                 x = i
#     print(f"LCM is Equal To :- {(n*m)//x}")
#     print(f"HCF is Equal To :- {x}")
#
#
#
#
#
#
# n = int(input("Enter First Number :- "))
# m = int(input("Enter Second Number :-"))
# LcmHcf(n,m)
def permute(n):
    finalString = []
    if len(n) == 0:
        finalString.append('')
        return finalString

    else:
        first = n[0]
        rest = n[1:]
        substring = permute(rest)

        for letter in substring:
            word = ''
            for j in range(0, len(letter)+1):
                word = letter[:j]+first+letter[j:]
                finalString.append(word)

        return finalString


print(permute('abc'))
