
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os


from_addr = '568779761@qq.com'
password = 'vqceufkhtnrbbdbi'
to_addr = '568779761@qq.com'

message = MIMEMultipart()
message['From'] = Header("张源<%s>" % from_addr, 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

with open("../report/result2.html", 'r', encoding='utf-8') as f:
    content = f.read()
    # 设置html格式参数
    part1 = MIMEText(content, 'html', 'utf-8')

    basename = os.path.basename("report.html")
# 添加一个txt文本附件
with open('../report/result2.html', 'r', encoding='utf-8') as h:
    content2 = h.read()
    # 设置txt参数
    part2 = MIMEText(content2, 'plain', 'utf-8')

    # 附件设置内容类型，方便起见，设置为二进制流
    part2['Content-Type'] = 'application/octet-stream'
    # 设置附件头，添加文件名
    part2['Content-Disposition'] = 'attachment;filename=%s' % basename

# 解决中文附件名乱码问题
# part2.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', basename))

message.attach(part1)
message.attach(part2)


smtp_server = 'smtp.qq.com'

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], message.as_string())
server.quit()