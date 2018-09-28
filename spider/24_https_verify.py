import requests

url1='https://baidu.com'
url2='https://www.12306.cn/'
rsp1=requests.request('get',url=url1)
requests.packages.urllib3.disable_warnings()
rsp2=requests.request('get',url=url2,verify=False)
print(rsp2.text)