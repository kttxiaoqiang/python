from urllib import error,request

if __name__=="__main__":
    url='http://www.baiiiiiiiiiiiidu.com'
    try:
        req=request.Request(url=url)
        rsp=request.urlopen(req)
        html=rsp.read().decode()
        print(html)
    except error.URLError as e:
        print("urlerror{}".format(e.reason) )
        print("urlerror{}".format(e))
    except Exception as e:
        print(e)