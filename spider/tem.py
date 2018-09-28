import urllib.request
import urllib.parse
import json
#
#
# content = input("Enter the words needs translated:")
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=ugc"
# data = {}
# data['i'] = content
# data['from'] = 'AUTO'
# data['to']='AUTO'
# data['smartresult']='dict'
# data['client']='fanyideskweb'
# data['salt']='1513663501217'
# data['sign']='6a516734349a812792c07491f639609e'
# data['doctype'] = 'json'
# data['version'] = '2.1'
# data['keyfrom']='fanyi.web'
# data['action']='FY_BY_REALTIME'
# data['typoResult']='false'
# data = urllib.parse.urlencode(data).encode('utf-8')
# response = urllib.request.urlopen(url,data)
# html = response.read().decode('utf-8')
# target = json.loads(html)
# print(target)
# print("result: %s" % (target['translateResult'][0][0]['tgt']))

from urllib import  request,error

proxy = {'http': '171.221.239.11:808'}  # 设置代理地址
proxy_handler = request.ProxyHandler(proxy)  # 创建proxy_handler
opener = request.build_opener(proxy_handler)
request.install_opener(opener)

url='http://10.0.88.224:82/#/main-page/apply?userId=14a3133c-d336-47e7-97af-916f406630af&token=linus'
rsp=request.urlopen(url)
html=rsp.read().decode()
print(html)