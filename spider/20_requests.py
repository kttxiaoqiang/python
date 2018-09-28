import requests
# url='http://www.baidu.com'
# rsp=requests.get(url)
# print(rsp.text)






url='http://www.baidu.com/s?'
kw={
    'wd':'乌龟蛋'
}

headers={
# 'Accept':'image/webp,image/*,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate, sdch, br',
# 'Accept-Language':'zh-CN,zh;q=0.8',
# 'Connection':'keep-alive',
# 'Cookie':'BIDUPSID=1E52240793639A1F5B822B2E6703345A; PSTM=1507619106; BAIDUID=DCB9C70BF6C6CDD097AFDBC3A9ABF80C:FG=1; __cfduid=dda522524ed3ccab1d2aad58544909b6e1517210786; BDUSS=HpmV3RQOExSejdzZnhMcWVkZTRPSVVDOGNwQkJUZEt3YTJiT3FGN1dvVW0weUJiQVFBQUFBJCQAAAAAAAAAAAEAAAA8m1E2w8jDyLXEsreytwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACZG-VomRvlaN; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=3; H_PS_PSSID=1454_21125_26350_20928',
# 'Host':'sp0.baidu.com',
# 'Referer':'https://www.baidu.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

rsp=requests.request('get',url=url,params=kw,headers=headers)
with open('./11_wendang/4.html','wb') as f:
    f.write(rsp.content)
print(rsp.text)
print(rsp.status_code)