import requests
'''
proxies={
    "http":"address of proxy"
    "https":"address of proxy"
}
'''
url='https://fanyi.baidu.com/sug'
data={
    'kw':'girl'
}

headers={

'Content-Length': str(len(data)),
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',

}

proxies={
    'http':'180.107.151.35:26073',
    # 'https':"42.202.130.216:808",
    # 'https':'118.190.215.65:80'
}

rsp=requests.post(url=url,data=data,headers=headers,proxies=proxies)
html=rsp.text
print(html)

'''
有时候会代理验证 格式为用户名：密码@代理地址：端口号(私密代理)
proxy={"http":"china:123456@192.168.1.123:80"}
rsp=requests.get(url,proxies=proxy)


web客户端验证:
如果遇到web客户端验证,需要添加auth验证（用户名和密码）
auth=("test1","123456")     授权信息
rsp=requests.get(url,auth=auth)

'''