#coding=utf-8
'''
定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。

Created on 2016-04-03
@author: RandyGuo
'''

def get_cjsum(int_num):
    cjsum = 0
    for i in range(1,int_num+1):
        num = i*i
        cjsum += num
    return cjsum
        
assert get_cjsum(100) == 338350
assert get_cjsum(3) == 14