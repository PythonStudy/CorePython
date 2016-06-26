#coding='utf-8'
"""
range(). What argument(s) could we give to the range()
built-in function if we wanted the following lists to be generated?
(a) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
(b) [3, 6, 9, 12, 15, 18]
(c) [-20, 200, 420, 640, 860]

"""

if __name__ == '__main__':
    a = [i for i in range(10)]
    print(a)
    b = [i for i in range(3,20,3)]
    print(b)
    c = [i for i in range(-20,861,220)] 
    print(c)