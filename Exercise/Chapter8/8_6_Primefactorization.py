#coding = utf-8

#Problem

"""
Prime Factorization. Take your solutions for isprime() and getfactors()
in the previous problems and create a function that takes an integer as input 
and returns a list of its prime factors. 
This process, known as prime factorization, should output a list of
factors such that if multiplied together, they will result in the original
number. Note that there could be repeats in the list. So if you
gave an input of 20, the output would be [2, 2, 5].

"""
# Difficulty: how to divide the factor to prime factors 
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

def factorization(int_num):
    if isinstance(int_num,int):
        factors = getfactors(int_num)
        prime_factors = []
        length = len(factors)
        for i in range(1,length-1):
            if isprime(factors[i]):
                prime_factors.append(factors[i])
                continue
        print(prime_factors)

factorization(100) 
        