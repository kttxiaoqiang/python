
from lxml import etree
'''
用lxml来解析HTML代码

'''
def etree1():
    text='''
    <div>
        <ul>
            <li class="item-0"><a herf="0.html"> first item </a></li>
            <li class="item-1"><a herf="1.html"> first item </a></li>
            <li class="item-2"><a herf="2.html"> first item </a></li>
            <li class="item-3"><a herf="3.html"> first item </a></li>
            <li class="item-4"><a herf="4.html"> first item </a></li>
            <li class="item-5"><a herf="5.html"> first item </a>
        </ul>
    </div>
    '''
    html=etree.HTML(text)
    s=etree.tostring(html)
    print(s)

def etree2():
    html=etree.parse('./11_wendang/07.xml')
    # rst=etree.tostring(html,pretty_print=True)
    # print(type(rst))
    # print(rst.decode())
    rst=html.xpath('//student[@Name="liuliu1"]')
    rst=rst[0]
    print(rst.tag)
    print(rst.text)
etree2()