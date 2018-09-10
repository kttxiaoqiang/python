import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg=MIMEText("hello world","plain","utf-8")


#这个是发件人
header_from=Header("从张翔邮箱发出去的<741257174@qq.com>","utf-8")
msg['From']=header_from
#这个是目的地
header_to=Header("目标地址<741257174@qq.com>",'utf-8')
msg['To']=header_to

header_sub=Header("这是张翔的主题",'utf-8')
msg['Subject']=header_sub




from_addr="741257174@qq.com"

from_pwd="hmsirppxzzvbbfjj"

to_addr="674136609@qq.com"

smtp_srv="smtp.qq.com"
try:
    #SSL是加密格式  有两个参数 一个是服务器地址，而且是要bytes格式，第二个是端口号 服务器接受访问的端口号
    srv=smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)   #登录邮箱

    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print(e)