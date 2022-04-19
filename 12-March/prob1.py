class rectangle:
    def __init__(self,l,b):
        self.length = l
        self.width = b

    def perimeter(self):
        return 2*(self.length + self.width)

    def area(self):
        return (self.length*self.width)
    def display(self):
        return self.perimeter(),self.area()
s1 = rectangle(8,10)
print(s1.display())
