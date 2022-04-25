# f = open('d.txt','r')
# print(f.mode)
# # f.close()
# f = open('b.txt','r')
# print(f.mode)



# f = open('b.txt','r')
# print(f.read())
# f = open('b.txt','a')
# f.write(' WRITTEN')
# f = open('b.txt','r')
# print(f.read())
# f.close()



f1 = open('b.txt','r')
print(f1.read())
f1.close()


f2 = open('b.txt','a')
f2.write("Written again")
f2.close()


f3 = open('b.txt','r')
print(f3.read())
print(f3.close())
f3.close()

# f1.close()
# f2.close()
# f3.close()
