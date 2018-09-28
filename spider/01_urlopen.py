from urllib import request
import requests


url='http://10.0.88.233:8080/icpm-web/ac/toDashboardAdmin?userId=14a3133c-d336-47e7-97af-916f406630af&token=1'
rsp=request.urlopen(url,timeout=10)
html=rsp.read()
print(rsp)
print(type(html))
print(html.decode())