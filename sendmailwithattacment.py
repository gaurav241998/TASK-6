import smtplib, ssl
import credentials
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Sender, Reciever, Body of Email
sender = credentials.mail
receivers = ['500068658@stu.upes.ac.in']
body_of_email = 'Hey gaurav it is 1st user face detected'

#Creating the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'Face_detected'
msg['From'] = sender
msg['To'] = ','.join(receivers)

#Adds a csv file as an attachment to the email 
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('./pic1.jpg', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="gaurav.jpg"')
msg.attach(part)

#Connecting to Gmail SMTP Server
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = credentials.mail, password = credentials.password)
s.sendmail(sender, receivers, msg.as_string())
s.quit()
print('MAIL SENT')