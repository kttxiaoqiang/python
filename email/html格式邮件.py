import smtplib
from email.mime.text import MIMEText

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


msg=MIMEText(mail_content,"html","utf-8")

from_addr="741257174@qq.com"

from_pwd="hmsirppxzzvbbfjj"

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