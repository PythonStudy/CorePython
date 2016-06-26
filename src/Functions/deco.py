#coding=utf-8
'''
Created on 2016-04-05
@author: RandyGuo
'''
from time import ctime,sleep
#tsfunc 显示何时调用函数的时戳的装饰器，
def tsfunc(func): 
    def wrappedFunc():
        print('[%s] %s() called' % (ctime(),func.__name__))
        return func()
    return wrappedFunc
@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
    
# [Tue Apr  5 20:48:43 2016] foo() called
# [Tue Apr  5 20:48:48 2016] foo() called
# [Tue Apr  5 20:48:49 2016] foo() called