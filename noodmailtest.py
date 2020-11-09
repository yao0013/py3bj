import smtplib
from email.mime.text import MIMEText
from email.header import Header

from_addr = '1697105397@qq.com'
password = 'nsgjjzlgusgteheh'

to_addrs = ['124203901@qq.com','ssi232@163.com']

smtp_server = 'smtp.qq.com'

text = '''床前明月光，
疑是地上霜，
举头望明月，
低头思故乡。'''
msg = MIMEText(text,'plain','utf-8')

# 邮件头信息
msg['From'] = Header('嘿嘿嘿')
msg['To'] = Header(",".join(to_addrs))
msg['Subject'] = Header('静夜思')


server = smtplib.SMTP_SSL(smtp_server) #端口用SSL加密这样写
server.connect(smtp_server, 465)

server.login(from_addr, password)


server.sendmail(from_addr, to_addrs, msg.as_string()) 
server.quit()