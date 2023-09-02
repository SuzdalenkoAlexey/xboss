import smtplib, ssl


sender_email = "xboss.developer@gmail.com"
receiver_email = "xboss.developer@gmail.com"
password = "doneqrmjfhbxlpwv"

message = {}
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """sdfgsdfgsdfg
"""



# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, "message.as_string()"
    )
