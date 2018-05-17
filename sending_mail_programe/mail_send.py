# using smtplib
import smtplib

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.ehlo()
connection.starttls()
connection.login('vikas807657@gmail.com','vikas15101992@')
connection.sendmail('vikas807657@gmail.com','vikaspal807657@gmail.com','hello how are you vikas!')
connection.quit()

print ("connect successfully msg send")
