#coding='utf-8'
'''
Created on 2016-04-16

@author: RandyGuo
'''
# ZeroDivisionError
try :
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x/y)
except ZeroDivisionError:
    print("The Second number can't be zero")
except NameError:
    print("Variable error!!")
except TypeError:
    print('Please input a number')
    
# define a class type
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division By zero is illegal")
            else:
                raise
