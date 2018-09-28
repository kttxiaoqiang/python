from bs4 import BeautifulSoup
import requests




def case1():
    url="httP://www.baidu.com"

    rsp=requests.get(url)
    html=rsp.content
    soup=BeautifulSoup(html,'lxml')
    html=soup.prettify()
    print(html)
# case1()

def case2():
    url="httP://www.baidu.com"

    rsp=requests.get(url)
    html=rsp.content
    soup=BeautifulSoup(html,'lxml')
    html=soup.prettify()
    print(html)
    print("*"*150)
    print(soup.head.prettify())
    print("*" * 150)
    print(soup.meta)
    print("*" * 150)
    print(soup.link)
    # print(soup.link.name)
    print(soup.link.attrs) #输出链接
    print("*" * 150)
    print(soup.title.string)#输出名称
    print("*" * 150)
    print(soup.name)
    print(soup.attrs)

# case2()

def case3():
    url="httP://www.baidu.com"

    rsp=requests.get(url)
    html=rsp.content
    soup=BeautifulSoup(html,'lxml')
    print("*" * 150)
    print(soup.head.contents)
    print("*" * 150)
    for i in soup.head.contents:
        print(i)
        if i.name=='title':
            print(i.string)

    print("*" * 150)

# case3()
def case4():
    import re
    url="httP://www.baidu.com"

    rsp=requests.get(url)
    html=rsp.content
    soup=BeautifulSoup(html,'lxml')
    # s=soup.find_all(name='meta')
    s=soup.find_all(name=re.compile(r'^me(.*)'))
    for i in s:
        print(i)
    print("*" * 150)

# case4()
def case5():
    import re
    url="httP://www.baidu.com"

    rsp=requests.get(url)
    html=rsp.content
    soup=BeautifulSoup(html,'lxml')
    print(soup.prettify())
    print("*" * 150)
    print(soup.select('title'))
    print("*" * 150)
    print(soup.select('meta[name="referrer"]'))


# case5()