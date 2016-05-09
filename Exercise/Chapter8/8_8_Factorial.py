#coding=utf-8

# Problem. Exercise 8-8
"""
Factorial. The factorial of a number is defined as the product
of all values from one to that number. A shorthand for N factorial
is N! where N! == factorial(N) == 1 * 2 * 3 * . . . * (N-2) *
(N-1) * N. So 4! == 1 * 2 * 3 * 4. Write a routine such that
given N, the value N! is returned.
"""
def factorial(int_num):
    if int_num <= 1 :
        return 1
    else :
        return factorial(int_num) * factorial(int_num -1)

print(factorial(4))