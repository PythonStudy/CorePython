#coding=utf-8
'''
Created on 2016年4月3日
Problem 2.2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
@author: RandyGuo
'''
import sys,os,urllib.request,urllib.parse
showlines = 6
try:
    servername,filename = sys.argv[1:3]
except:
    servername,filename = 'www.baidu.com','/index.html'

remoteaddr = 'http://%s%s' % (servername,filename) # 任何网络地址
if len(sys.argv) == 4:
    localname = sys.argv[3]
else:
    (scheme,server,path,parms,query,frag) = urllib.parse.urlparse(remoteaddr)
    localname = os.path.split(path)[1]

print(remoteaddr,localname)
urllib.request.urlretrieve(remoteaddr,localname)
remotedata = open(localname,'rb').readlines()
for line in remotedata[:showlines]:
    print(line)
