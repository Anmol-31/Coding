# def SieveOfEratosthenes(n):
#
#     '''Create a boolean array "prime[0..n]" and initialize
#      all entries it as true. A value in prime[i] will
#      finally be false if i is Not a prime, else true.'''
#     prime = [True for i in range(n + 1)]
#     p = 2
#     while (p * p <= n):
#
#         # If prime[p] is not changed, then it is a prime
#         if (prime[p] == True):
#
#             # Update all multiples of p
#             for i in range(p ** 2, n + 1, p):
#                 prime[i] = False
#         p += 1
#     prime[0]= False
#     prime[1]= False
#     # Print all prime numbers
#     for p in range(n + 1):
#         if prime[p]:
#             print (p,end=' ') #Use print(p) for python 3
#
# # driver program
# if __name__=='__main__':
#     n = 30
#     print ("Following are the prime numbers smaller", end=' ')
#     #Use print("Following are the prime numbers smaller") for Python 3
#     print ("than or equal to", n)
#     #Use print("than or equal to", n) for Python 3
#     SieveOfEratosthenes(n)














def tower_of_hanoi(disks, source, auxiliary, target):
    if(disks == 1):
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))
        return
    # function call itself
    tower_of_hanoi(disks - 1, source, target, auxiliary)
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))
    tower_of_hanoi(disks - 1, auxiliary, source, target)


disks = int(input('Enter the number of disks: '))
# We are referring source as A, auxiliary as B, and target as C
tower_of_hanoi(disks, 'A', 'B', 'C')  # Calling the function
