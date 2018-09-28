#cookie 在本地 session在服务器上 即存放位置不一致
#cookie不安全
#session会保存在服务器上一段时间
from urllib import  request,error

proxy = {'http': '171.221.239.11:808'}  # 设置代理地址
proxy_handler = request.ProxyHandler(proxy)  # 创建proxy_handler
opener = request.build_opener(proxy_handler)
request.install_opener(opener)

url='http://www.renren.com/'
headers={
    "cookie":"ick_login=1d837e08-ed5e-4686-bd1a-ec3b9b793656; anonymid=jm7io9im-nxzdgl; depovince=JS; jebecookies=70802ff3-e7d5-4064-b912-a6ecbd583aff|||||; _r01_=1; JSESSIONID=abcWGtsEGwgH84_Q3aSxw; ick=ac6d040a-9001-4be5-90b1-127830a5a2f0; __utma=151146938.1415364427.1537263025.1537263025.1537263025.1; __utmc=151146938; __utmz=151146938.1537263025.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=151146938.1.10.1537263025; _de=563B31CD69CA840C3F16E7D5D4146F99; p=4d6c4642d0dbb91721a1ee49b74054889; first_login_flag=1; ln_uact=13913592933; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20100320/2135/h_main_0UsG_31aa000061da2f75.jpg; t=270de851aaf94360d944178e35b63d079; societyguester=270de851aaf94360d944178e35b63d079; id=263834919; xnsid=13fb5529; jebe_key=050602f4-05a9-49cb-95a0-09f45b01c5ea%7C064916ad2a31c63438ddb96d1aa78483%7C1537263056603%7C1%7C1537263066859; wp_fold=0; ver=7.0; loginfrom=null"
}
req=request.Request(url=url,headers=headers)
rsp=request.urlopen(req)
html1=rsp.read()
with open('./11_wendang/1.html','wb') as f:
    f.write(html1)
print(html1)


