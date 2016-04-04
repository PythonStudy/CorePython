#coding=utf-8
'''
Created on 2016-04-04
一：定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int


写好类以后，可以定义2个同学测试下:

zm = student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100

lq = student('liqiang',23,[82,60,99])

返回结果：
liqiang
23
99

@author: RandyGuo
'''

class student(object):
    '''
    Student Class
    '''

    def __init__(self, name,age,score_list):
        '''
        init student information
        '''
        self.name = name
        self.age = age
        self.score = score_list
        if not isinstance(self.name,str):
            print("Student name must be a string!!!")
        if not isinstance(self.age,int):
            print("Student name must be a int type!!!")
        if not isinstance(self.score,list):
            print("Student score must be a list type")
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_score(self):
        self.score.sort()
        return self.score[2]

zm = student('zhangming',20,[69,88,100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_score())
assert zm.get_name() == "zhangming"
assert zm.get_age()  == 20
assert zm.get_score() == 100

lq = student('liqiang',23,[82,60,99])
print(lq.get_name())
print(lq.get_age())
print(lq.get_score())
assert lq.get_name() == 'liqiang'
assert lq.get_age() == 23
assert lq.get_score() == 99