#coding=utf-8
"""
Factors. Write a function called getfactors() that takes a
single integer as an argument and returns a list of all its factors,
including 1 and itself

"""
def getfactors(int_num):
    factors = []
    if isinstance(int_num,int):
        for factor in range(1,int_num//2+1):
            if int_num % factor == 0:
                factors.append(factor) # it will not add themselves as the factors, so we must add themselves add the last factors
    else:
        print("Please input a integer number:")
    factors.append(int_num)
    return factors
    
print("Number  1 has factors: ",getfactors(1))
print("Number  2 has factors: ",getfactors(2))
print("Number 12 has factors: ",getfactors(12))

assert getfactors(10) == [1,2,5,10]
assert getfactors(12) == [1,2,3,4,6,12]