__author__ = 'RandyGuo'

class FirstClass:
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Current Value = %s' % self.data)

x = FirstClass()
y = FirstClass()
z = SecondClass()

z.setdata(42)
x.setdata("King Arthur")
y.setdata(3.14159)

x.display()
y.display()
z.display()
