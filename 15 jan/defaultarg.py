'''Types of arguments Values'''

# def display(a,b=4,c='Hello World'):
#     print(a,b,c,sep='    ')
#
#
# display(1)
# display(8)
# display(10)
# # display(1,2)
# # display(1,2,3)
# # display()

'''
Default Agrument Value

Default value is executed only once.

order matter in default argument
'''
# def display(a,b=4,c='Hello World',d=[]):
#     print(a,b,c,d,sep='    ')
#     b=b+6
#     d.append(a)
#
#
# display(1)
# display(8)
# display(10)
def display(a,b=4,c='Hello World'):
    print(a,b,c,sep='    ')
    b = b + 6
    #print(f'The id of b is {id(b)}')
    print('**********************')


display(1)
display(1)
display(1)
