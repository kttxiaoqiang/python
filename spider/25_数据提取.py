
def case1():
    import re
    s = r'([a-z]+) ([a-z]+)'
    pattern=re.compile(s,re.I)
    m=pattern.match("hello world wide web")
    s=m.group(0)
    print(s)
    s=m.group(2)
    print(s)
    a=m.span(0)
    print(a)

    s=m.groups()
    print(s)

#match 从开始位置查找，一次匹配
#search 从任何位置查找，一次性匹配
#findall 全部匹配 返回列表
#finditer 全部匹配 返回迭代器
#split 分割字符串 返回列表
#sub 替换

def case_search():
    import re
    s='\d+'
    t='555one123two234three332'
    p=re.compile(s,re.I)
    s1=p.match(t)
    print(s1)
    s2=p.search(t,pos=6)
    print(s2)
    s3=p.findall(t)
    print(s3)
    s4=p.finditer(t)
    for i in s4:
        print(i)
    s5=t.split('e')
    print(s5)
    s6=re.sub(s,'999',t)
    print(s6)
# case_search()

def case_chinese():
    import re
    hello=u'你好，世界'
    p=re.compile(r'[\u4e00-\u9fa5]+') #这个是中文
    s1=p.match(hello)
    s2=p.findall(hello)
    print(s1)
    print(s2)
case_chinese()