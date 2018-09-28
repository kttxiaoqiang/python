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


class baidu():
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        self.url='http://fanyi.baidu.com/sug'
# baseurl='http://fanyi.baidu.com/sug'
    def begin(self):
        kw=input('输入需要查询的内容:')
        data={
            'kw':kw
        }
        data=parse.urlencode(data)
        data=data.encode()

        headers={
            'Content-Length':len(data)
        }
        rsp=request.urlopen(self.url,data=data)
        json_data=rsp.read().decode('utf-8')
        print(json_data)
        json_data=json.loads(json_data)
        print(json_data)
if __name__=="__main__":
    b=baidu()
    b.begin()