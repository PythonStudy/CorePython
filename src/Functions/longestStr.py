#coding='utf-8'
'''
Created on 2016-04-02
Problem 2: define a function , give random string parameters , return the longest string
@author: RandyGuo
'''

def longStr(*strs):
    longest = strs[0]
    for string in strs:
        if isinstance(string,str):
            if len(longest) <= len(string):
                longest = string
        else:
            print("The param in strings given ,is not a str type!!")
    return longest
    

if __name__ == '__main__':
    testStrs = ("12",'abcde',"adcdakfdal",'adfjlakfdjla','kalf','adfakjfldfafdasafa','lajfdaf','a','laflal')
    longestStr = longStr("12",'abcde',"adcdakfdal",'adfjlakfdjla','kalf','adfakjfldfafdasafa','lajfdaf','a','laflal')
    print("All strings are : \n ",testStrs)
    print("The longest sring is : " , longestStr)