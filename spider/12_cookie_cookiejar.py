from urllib import request,parse
from http import cookiejar
#创建cookiejar的实例
cookie=cookiejar.CookieJar()
#生成cookie的管理器
cookie_handler=request.HTTPCookieProcessor(cookie)
#创建http的请求管理器
http_handler=request.HTTPHandler()
#创建https管理器
https_handler=request.HTTPSHandler()
#创建请求管理器
opener=request.build_opener(http_handler,https_handler,cookie_handler)
def login():
    '''
    验证初次登录用
    '''
    url='http://www.renren.com/PLogin.do'
    data={
        'email':'13913592933',
        'password':'0816403011'
    }
    data=parse.urlencode(data)
    data=data.encode()
    req=request.Request(url=url,data=data)
    rsp=opener.open(req)

def logined():
    url ='http://www.renren.com/263834919/profile?v=info_timeline'
    rsp=opener.open(url)
    rsp=rsp.read()
    with open('./11_wendang/2.html','wb') as f:
        f.write(rsp)

if __name__=="__main__":
    login()
    logined()
