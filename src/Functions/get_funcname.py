#coding=utf-8
'''
定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
类型为str)，否则返回 “fun is not function"。
Created on 2016-04-03
@author: RandyGuo
'''
global var_func
var_func = 10

def func_test():
    pass

def get_funcname(func):
    if type(get_funcname) != type(func):
        return "fun is not function"
    else:
        return func.__name__

if __name__ == '__main__':
    print(type(get_funcname))
    print(type(func_test))
    print(type(type.__call__))
    print(type(get_funcname) == type(func_test))
    assert get_funcname(var_func) == "fun is not function"
    print(get_funcname(func_test))