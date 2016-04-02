#coding='utf-8'
'''
Created on 2016��4��2��
1.����һ������ func����func�����������������Ͳ�����������������С��ֵ��
@author: RandyGuo
'''
def maxAndMin(*nums):
    maxNum=nums[0]
    minNum=nums[0]
    for number in nums:
        if isinstance(number,int):
            if maxNum <= number:
                maxNum = number
            if minNum >= number:
                minNum = number
        else :
            print("There is a non int type in the parameter list.")
    return maxNum,minNum
            

if __name__ == '__main__':
    testNums = (2,3,4,1,21,31,20,19,100)
    maxNumber,minNumber = maxAndMin(2,3,4,1,21,31,20,19,100)
    print("All number are : \n ",testNums)
    print("The MaxNumber is : %d , the min number is : %d " % (maxNumber,minNumber))