# using smtplib
import smtplib



"""
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.ehlo()
connection.starttls()
connection.login('vikas807657@gmail.com','vikas15101992@')
connection.sendmail('vikas807657@gmail.com','vikaspal807657@gmail.com','hello how are you vikas!')
connection.quit()

print ("connect successfully msg send")

"""


#input admin email_id_

email_id = input("enter your email id : ")
print (email_id)
password =  input("enter your password: ")
print (password)


def is_valid_email_id(email_id):
    domain_name = ["gmail",'yahoo','outlook','hotmail']
    if '@' in email_id and '.' in email_id :
        symbol_pos = email_id.find('@')
        dotcom_pos = email_id.find(".com")
        domain = email_id[symbol_pos+1 : dotcom_pos]
        print(domain)
        if domain in domain_name:
            return  email_id , domain
        else:
            print('we dont provide service '+ domain)
            print ('we provide only services : gmail/yahoo/outlook/hotmail')
    




    else:
         print("invalid email id")


email , domain = is_valid_email_id(email_id)
print(email)
print(domain)
print(domain)

