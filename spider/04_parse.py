import urllib
'''
掌握对参数进行编码
使用parse.urlencode

'''
from urllib import request,parse
if __name__=="__main__":
    url='http://www.baidu.com/s?'
    wd=input('input your keyword')
    qs={"wd":wd}
    qs=parse.urlencode(qs)
    full_url=url+qs
    print(full_url)
    rsp=urllib.request.urlopen(full_url)
    print(type(rsp))
    print(rsp)
    rsp=rsp.read()
    print(rsp.decode())


