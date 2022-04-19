# a=5
# def outer():
#     a = 10
#     def inner():#nested func.
#         a = "anmol"
#         print(a)
#     inner()
#     print('outer function')
#     print(a)
# outer()
# print(a)



a=5
def outer():
    a = 10

    def inner():#nested func.
        nonlocal a
        print('Inner Function')
        a='xx'

        print(a)
    inner()
    print('outer function')
    print(a)
outer()
print(a)
