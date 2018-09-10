from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
import smtplib

mail_mul=MIMEMultipart()
#构建邮件的正文
mail_text=MIMEText("hello i am python","plain","utf-8")

mail_mul.attach(mail_text)

with open ("02.html","rb") as f:
    s=f.read()
    m=MIMEText(s,'base64',"utf-8")
    m["content-Type"]="application/octet-stream"

    m["content-Disposition"]="attachment;filename='02.html'"
    mail_mul.attach(m)


from_addr="741257174@qq.com"

from_pwd=""  #授权码

to_addr="741257174@qq.com"

smtp_srv="smtp.qq.com"
try:
    #SSL是加密格式  有两个参数 一个是服务器地址，而且是要bytes格式，第二个是端口号 服务器接受访问的端口号
    srv=smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)   #登录邮箱

    srv.sendmail(from_addr,[to_addr],mail_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)