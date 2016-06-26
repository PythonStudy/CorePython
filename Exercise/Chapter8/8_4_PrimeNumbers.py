#coding=utf-8

"""
Prime Numbers. We presented some code in this chapter to determine a number’s largest factor or if it is prime. Turn this
code into a Boolean function called isprime() such that the input is a single value, and the result returned is True if
the number is prime and False otherwise.
"""

def isprime(int_num):
    result = True
    if int_num <=0 or not isinstance(int_num,int):
        #print("Please give a int number bigger than 0")
        raise Exception("Please give a int number bigger than 0")
    if int_num == 1 or int_num == 2:
        return True
    for factor in range(2,int_num//2+1):
        if (int_num % factor == 0):
            result = False
    return result

assert isprime(2) == True
assert isprime(1) == True
assert isprime(3) == True
assert isprime(6) == False
assert isprime(12) == False
