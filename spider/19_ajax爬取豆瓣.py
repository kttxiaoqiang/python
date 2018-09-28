from urllib import request,parse
import json
url='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20'

rsp=request.urlopen(url)
html=rsp.read().decode()
html=json.loads(html)
# print(html)
# print(type(html))
print(len(html))
for i in html:
    print(i)