#coding = 'utf-8'

#Exercise 8.7 
"""
Perfect Numbers. A perfect number is one whose factors (except
itself) sum to itself. For example, the factors of 6 are 1, 2, 3, and 6.
Since 1 + 2 + 3 is 6, it (6) is considered a perfect number. Write a
function called isperfect() which takes a single integer input
and outputs 1 if the number is perfect and 0 otherwise.
"""

def isperfect(int_num):
    factor_sum = 0
    factors = []
    for factor in range(1,int_num//2 +1):
        #print(factor)
        if int_num % factor == 0:
            factors.append(factor)
            factor_sum += factor
    #print('factors are ',factors)
    #print('factor_sum is ',factor_sum)
    #print('int number is : ',int_num)
    if factor_sum == int_num:
        return 1
    else:
        return 0

def find_isperfect(int_num = 100):
    perfect_nums = []
    for number in range(1,int_num):
        if isperfect(number) == 1:
            perfect_nums.append(number)
    return perfect_nums

isperfect_nums = find_isperfect(100)
print("perfect numbers in range are ")
print(isperfect_nums)

assert isperfect(6) == 1
assert isperfect(18) == 0
assert isperfect(28) == 1
