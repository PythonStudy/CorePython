__author__ = 'RandyGuo'
#coding=utf-8
"""
split and interactively page a string , file , or stream of text to stdout ; when run as a script,
page stdin or file whose name is passed on  cmdline ; if input is stdin,can't use it for user reply
--use platform--specific tools or GUI;

"""

import sys

def getreply():
    '''
    读取交互式用户的回复键，即使stdin重定向到某个文件或者管道
    '''
    if sys.stdin.isatty():
        return input('?')       # 如果stdin 是控制台 从stdin 读取回复行数据
    else :
        if sys.platform[:3]  == 'win':   # 如果stdin 重定向，不能用于询问用户
            import msvcrt
            msvcrt.putch(b'?')
            key = msvcrt.getche()        # 使用windows 控制台工具 getch()方法不能回应键
            return key
        else:
            assert False,'platform not supported'
            #linux?:open(/dev/tty).readline()[:-1]

def more(text,numlines = 10):
    """
    page multiline string to stdout
    :param text:
    :param numlines:
    :return:
    """
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:print(line)
        if lines and getreply() not in [b'y',b'Y']:break

if __name__ == '__main__':
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1].read()))
