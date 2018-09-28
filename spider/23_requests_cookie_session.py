'''
cookie和session
创建一个session对象可以保持cookie值
'''
def this_cookie():
    import requests
    url='http://fanyi.youdao.com'
    rsp=requests.get(url)

    cookiejar=rsp.cookies

    print(cookiejar)

    cookies=requests.utils.dict_from_cookiejar(cookiejar)

    print(type(cookies))
    print(cookies)

def this_session():
    url='http://www.baidu.com/s?'
    import requests
    ss=requests.session()
    # headers={
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    # }
    headers = {
        # 'Cookie': 'BIDUPSID=1E52240793639A1F5B822B2E6703345A; PSTM=1507619106; BAIDUID=DCB9C70BF6C6CDD097AFDBC3A9ABF80C:FG=1; __cfduid=dda522524ed3ccab1d2aad58544909b6e1517210786; BDUSS=HpmV3RQOExSejdzZnhMcWVkZTRPSVVDOGNwQkJUZEt3YTJiT3FGN1dvVW0weUJiQVFBQUFBJCQAAAAAAAAAAAEAAAA8m1E2w8jDyLXEsreytwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACZG-VomRvlaN; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=3; H_PS_PSSID=1454_21125_26350_20928',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

    kw={
        'wd':'乌龟蛋'
    }

    ss.get(url=url,params=kw,headers=headers)
    rsp=ss.get(url,params=kw)
    for i in rsp.cookies:
        print(i)
    # print(rsp.cookies)
    with open('./11_wendang/6.html','wb') as f:
        f.write(rsp.content)
    print(rsp.content)
this_session()