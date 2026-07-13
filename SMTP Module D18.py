'''
#SMTP Module
#email.message
import smtplib
import ssl
from email.message import EmailMessage
sender_email="lokeshwar5221@gmail.com"
password="bkdfvnjpblgfmdkr"

receiver_email="lokeshwar2512@gmail.com"
message=EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="welcome mail"
message.set_content("welcome to loki univers")

context=ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)

'''

import smtplib
from email.message import EmailMessage
sender_email="lokeshwar5221@gmail.com"
password="bkdfvnjpblgfmdkr"

receiver_email="lokeshwar2512@gmail.com"
message=EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="welcome mail"
message.set_content("""
welcome to loki univers

i think your are doing good at your life

stay strong towards your emotions

your all desires will come true one day just keep going""")

try:
    smtp=smtplib.SMTP("smtp.gmail.com",port=587)
    smtp.starttls()
    smtp.login(sender_email,password)
    smtp.send_message(message)
    print("Email sent successfilly")
except Exception as e:
    print("error:",e)
finally:
    smtp.quit()
