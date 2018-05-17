import mail_send
import smtplib

print("Welcome you can send an E-mail through this programe")
print("enter you E-mail and password")
email , domain = mail_send.get_email_id()

password = input('Password: ')
smtpDomain = mail_send.set_smtp_domain(domain)

print("Please type receivers E-mail")
reciever_email,receiver_domain = mail_send.get_email_id()
print("Now type Subjects and Message")
Subject = input("Subject: ")
Message = input("Message: ")


"""

connection = smtplib.SMTP(mail_send.smtpDomain, 587)
connection.ehlo()
connection.starttls()
connection.login(mail_send.email,mail_send.password)
connection.sendmail('vikas807657@gmail.com','vikaspal807657@gmail.com','hello how are you vikas!')

print ("E-mail send successfully")

connection.quit()




"""
