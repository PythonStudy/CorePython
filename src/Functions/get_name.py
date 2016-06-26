#coding=utf-8
'''
Created on 2016-04-02
习题 2.1定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：
（注：列表里面的元素为偶数）。
@author: RandyGuo
'''

def get_num(num):
    assert type(num) == type([])
    evenNum = []
    #Check the members in the list which can only contain int number. 
    for number in num:
        if not isinstance(number,int):
            print("There is a non-int member,please ensure all the members in the list are Int Types!!")
            return None
        if number % 2 == 0:
            evenNum.append(number)
    return evenNum

assert get_num([12,34,11,21,15,22,4,0,5]) == [12,34,22,4,0]
assert get_num([12,'23',123,11,10]) == None