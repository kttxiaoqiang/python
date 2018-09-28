import urllib
from urllib import request
import chardet
if __name__=="__main__":
    url='http://stock.eastmoney.com/news/1407,20170807763593890.html'
    rsp=request.urlopen(url)
    print(rsp)
    html=rsp.read()
    # print(html.decode())
    cs=chardet.detect(html)   #chardet 检查编码方式
    print(type(cs))
    print(cs)
    html=html.decode(cs.get("encoding","utf-8"))
    print(html)