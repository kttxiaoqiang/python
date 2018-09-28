'''
利用parse模拟post请求
分析百度词典
分析步骤
1.打开F12
2.尝试输入girl，实现一个字母后请求
3.请求地址是http://fanyi.baidu.com/sug
4.利用Network-All-Headers查看发现FormData是kw：girl
5.检查返回内容的格式
'''
from urllib import request,parse
import json
import re
import time

class baidu():
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        # self.url='http://fanyi.baidu.com/sug'
        self.url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# baseurl='http://fanyi.baidu.com/sug'
    def begin(self):
        global kw
        kw=input('输入需要查询的内容:')
        data={
            'i':kw,
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt':'1537174449228',
            'sign':'88f550eb79c26a903b5410d92b8f3979',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_REALTIME',
            'typoResult':'false'
        }
        data=parse.urlencode(data)
        data=data.encode()


        # rsp=request.urlopen(self.url,data=data)
        req=request.Request(url=self.url,data=data,headers=self.headers)
        rsp=request.urlopen(req)
        json_data=rsp.read().decode('utf-8')
        # print(json_data)
        # print(type(json_data))
        json_data=json.loads(json_data)
        # print(json_data)
        # print(type(json_data))
        # print(json_data['translateResult'])
        # print(type(json_data['translateResult']))
        print('result:{}'.format(json_data['translateResult'][0][0]['tgt']))
if __name__=="__main__":
    b=baidu()
    while 1:
        b.begin()
        if kw=='exit':
            exit()
