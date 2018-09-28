'''
1.设置代理地址
2.创建ProxyHandler
3.创建opener
4.安装opener
'''
# import urllib
# from urllib import request,error
# if __name__=="__main__":
#     url='http://www.baidu.com'
#     proxy={'http':'171.221.239.11:808'}
#     proxy_handler=request.ProxyHandler(proxy)
#     opener=request.build_opener(proxy_handler)
#     request.install_opener(opener)
#     try:
#         rsp=request.urlopen(url)
#         html=rsp.read().decode()
#         print(html)
#     except error.URLError as e:
#         print(e)
#     except Exception as e:
#         print(e)




from urllib import  request,error,parse
import json
if __name__=="__main__":
    url='https://fanyi.baidu.com/sug'



    proxy={'http':'171.221.239.11:808'} #设置代理地址
    proxy_handler=request.ProxyHandler(proxy)                      #创建proxy_handler
    opener=request.build_opener(proxy_handler)
    request.install_opener(opener)
    try:
        kw=input('输入要翻译的内容：')
        data={
            'kw':kw
        }
        data=parse.urlencode(data)
        data=data.encode()

        req=request.Request(url=url,data=data)
        rsp=request.urlopen(req)
        html=rsp.read().decode()
        # html=json.load(html)
        # print(type(html))
        json_data=json.loads(html)
        # print(type(json_data))
        # print(json_data['data'])
        json_data=json_data['data']
        for i in json_data:
            print(i['v'])
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)