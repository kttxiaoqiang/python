from urllib import request,parse
from http import cookiejar
#创建cookiejar的实例
# filename='cookie.txt'
cookie=cookiejar.MozillaCookieJar(filename='./11_wendang/cookie.txt')
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
    cookie.save(ignore_discard=True,ignore_expires=True) #无视过期


if __name__=="__main__":
    login()

