import urllib
from urllib import request
if __name__=="__main__":
    url='http://stock.eastmoney.com/news/1407,20170807763593890.html'
    rsp=urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print("url: {}".format(rsp.geturl()))
    print("info: {}".format(rsp.info))
    print("code:{}".format(rsp.getcode()))