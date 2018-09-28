import urllib
from urllib import request,error
if __name__=="__main__":
    url='http://www.baidu.com'
    try:
        headers={}
        headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        req=request.Request(url=url,headers=headers)
        rsp=request.urlopen(req)
        html=rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print("HTTPERROR:{}".format(e.reason))
        print("HTTPERROR:{}".format(e))
    except error.URLError as e:
        print("URLError:{}".format(e.reason))
        print("URLError:{}".format(e))
    # except Exception as e:
    #     print(e)