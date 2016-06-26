#!/usr/bin/env python
#coding=utf-8
#Python 2.7
'''
Created on 2016-04-05
@author: RandyGuo
'''
from operator import add,sub
from random import randint,choice
#Glob variable define 
ops ={'+':add,'-':sub}
MAXTRIES = 2 # Try 2 times before you give right answer

def doprob():
    op = choice('+-') # Select a operation random
    nums = [randint(1,10) for i in range(2)] # select two random numbers
    nums.sort(reverse=True) 
    ans = ops[op](*nums) # add(1,2) = 3, sub(5,4) =1
    pr = '%d %s %d = ' % (nums[0],op,nums[1]) 
    oops = 0
    while True:
        try:
            if int(input(pr)) == ans:
                print('Correct!')
                break
            if oops == MAXTRIES:
                print('answer\n%s%d' % (pr,ans)) # More than 2 times ,give the right answer
            else: # oops add 1 if give the incorrect answer 
                print('Incorrect...Try again')
                oops+=1 
        except (KeyboardInterrupt,EOFError,ValueError):
            print('invalid input ..... try again')
def main():
    while True:
        doprob()
        try :
            opt =input('Again?[y]').lower()
            if opt and opt[0] == 'n':
                break
        except(KeyboardInterrupt,EOFError):
            break

if __name__ == '__main__':
    main()