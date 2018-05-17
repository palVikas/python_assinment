# using smtplib
import smtplib



#input admin email_id_


def get_email_id():
    domain_name = ["gmail",'yahoo','outlook','hotmail']
    while True:
        email_id = input("E-mail: ")
        if '@' in email_id and '.' in email_id :
            symbol_pos = email_id.find('@')
            dotcom_pos = email_id.find(".com")
            domain = email_id[symbol_pos+1 : dotcom_pos]
            if domain in domain_name:
                return  email_id , domain
                break
            else:
                print('we dont provide service '+ domain)
                print ('we provide only services : gmail/yahoo/outlook/hotmail')
                continue
        else:
             print("invalid email id")
             continue


def set_smtp_domain(serviceProvider):
    if serviceProvider == 'gmail':
        return 'smtp.gmail.com'
    if serviceProvider == 'outlook' or seviceProvider == 'hotmail':
        return 'smtp-mail.outlook.com'
    if serviceProvider == 'yahoo':
        return 'smtp.mail.yahoo.com'




