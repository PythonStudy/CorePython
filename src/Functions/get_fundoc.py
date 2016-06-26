#coding=utf-8
'''
Created on 2016年4月3日
1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
@author: RandyGuo

'''

from Functions import get_name
from Functions import IDCheck

def get_fun_doc(func):
    if func.__doc__ == None:
        return "not found"
    else:
        print(func.__doc__)
        return func.__doc__
    

assert get_fun_doc(get_name.get_num) == "not found"
get_fun_doc(IDCheck.idcheck)
#assert get_fun_doc(IDCheck.idcheck) == "    Judge the identifier whether is a right identifier or not. "
#Two problem: 1, It will always display the print expression when call the function whose has print expression.
#2. It always 