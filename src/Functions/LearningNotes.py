#coding=utf-8
'''
Created on 2016-04-05
@author: RandyGuo
'''
'''
def hello():
    print("hello world")

if __name__ == '__main__':
    res = hello()
    print(res) # return None 函数无返回值
'''

#函数返回值 
'''
def foo():
    return ['xyz',100000,-98.6]

def bar():
    return 'abc',[42,'python'],'Guido'
# same as 
def bar_tuple():
    return ('abc',[42,'python'],'Guido')

print(bar())
print(bar_tuple())

'''

#前向引用
#Python 不允许在函数未声明之前，对其进行引用或者调用。
"""
def foo():
    print('in foo()')
  #  bar() # NameError: global name 'bar' is not defined
foo()

"""
'''
def bar():
    print("in bar()")

def foo():
    print('in foo()')
    bar()  # bar in here can be called ,because it has been defined before be called.
foo()
'''
"""
#我们可以在函数bar()前定义函数foo()
def foo():
    print('in foo()')
    bar()
def bar():
    print('in bar()')
foo()

#foo()函数的调用发生在bar()函数的声明之后，所以可以正常调用bar(). 换句或说，我们声明 foo()，然后再声明 bar(),接着调用foo().调用之前bar()已经存在了
"""
"""
#函数属性
def foo():
    'foo() --- properly created doc string'
def bar():
    pass
bar.__doc__ = 'Oops, forgot the doc str above'
bar.version = 0.1

help(foo)
'''
Help on function foo in module __main__:

foo()
    foo() --- properly created doc string
'''
print(bar.version)
#0.1
print(foo.__doc__)
#foo() --- properly created doc string
print(bar.__doc__)
#Oops, forgot the doc str above
"""

