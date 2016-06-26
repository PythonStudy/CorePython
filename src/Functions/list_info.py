#coding=utf-8
'''
problem: 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：

a = [1,2,3]

def list_info(list):
   要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了

print list_info(a):返回结果：[1,2,5]

print a 输出结果：[1,2,3]

写出函数体内的操作代码。


Created on 2016-04-03
@author: RandyGuo
'''
def list_info(num_list):
    nums = num_list[:] #copy the origin list ,then if you do some actions will not affect the origin list.
    nums[2] = 5
    return nums

a = [1,2,3]
assert list_info(a) == [1,2,5]
assert a == [1,2,3]