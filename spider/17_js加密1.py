from urllib import request,error,parse
import json

def youdao(key):
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data={
    "i": key,
    'from':'AUTO',
    'to': 'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1537325708401',
    'sign':'664780a58d9dc420f218bbc65f2744e5',
    'doctype':'json',
    'version':'2.1',
    'keyfrom': 'fanyi.web',
    'action':'FY_BY_REALTIME',
    'typoResult':'false'
    }
    data=parse.urlencode(data).encode()
    headers={
        'ccept':'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Content-Length':'200',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'_ntes_nnid=c38617702031847040178d1214582f81,1508204967553; OUTFOX_SEARCH_USER_ID_NCOO=961474810.6112236; OUTFOX_SEARCH_USER_ID=-457521813@58.209.218.213; JSESSIONID=aaay8LburU0F-f6jdWVxw; ___rl__test__cookies=1537325708388',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    req=request.Request(url=url,data=data,headers=headers)
    rsp=request.urlopen(req)
    html=rsp.read().decode()
    print(html)
    html=json.loads(html)
    print(html)
    print(type(html))
    print(html['translateResult'][0][0]['tgt'])
    # print(type(html['smartResult']['entries']))
    print(html['smartResult']['entries'][1])


youdao('girl')