import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



msg=MIMEMultipart('alternative')

head_from=Header("从发出者这里发出的","utf-8")
msg["From"]=head_from

head_to=Header("到接受者","utf-8")
msg["TO"]=head_to

head_sub=Header("摘要信息","utf-8")
msg["Subject"]=head_sub


#设置html格式的内容
mail_content='''
            <!DOCTYPE html>
            <html lang='en'>
            <head>
                <meta charset="utf-8"
                <titile>TITLE</title>
            </head>
            <body>
            <h1>这是一封html格式的邮件</h1>
            </body>
            </html>
            '''


msg_html=MIMEText(mail_content,"html","utf-8") #设置内容为html格式
msg.attach(msg_html)


msg_text=MIMEText("just text content","plain","utf-8") #设置纯文本格式
msg.attach(msg_text)

from_addr="741257174@qq.com"

from_pwd=""  #次数输入授权码

to_addr="741257174@qq.com"

smtp_srv="smtp.qq.com"
try:
    #SSL是加密格式  有两个参数 一个是服务器地址，而且是要bytes格式，第二个是端口号 服务器接受访问的端口号
    srv=smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)   #登录邮箱

    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print(e)