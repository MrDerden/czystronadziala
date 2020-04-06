import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'adres@mail'
PASSWORD = 'hasło'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    #names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            #names.append(a_contact.split()[0])
            #emails.append(a_contact.split()[1])
            emails.append(a_contact.split()[0])
    return emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
>>>>>>> dca5bea4329e7c1713305c0c41f82c0d3577dded

def main(site_name, err_code, reason):
    emails = [
        'mail@mail.pl', 
        'mail2@akcjademokracja.pl'
        ]

    # set up the SMTP server
    s = smtplib.SMTP(host='ssl0.ovh.net', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for email in emails:
        msg = MIMEMultipart()       # create a message
        
        #BEZ POLSKICH ZNAKOW
        message = 'Uwaga! Jedna ze stron nie dziala!\n'
        message += "\n"
        message += "Strona {} zwraca blad\n".format(site_name)
        message += "Kod bledu: {}\n".format(err_code)
        message += "Opis bledu: {}\n".format(reason)
        message += "\n"
        message += "Synology Serwer"
        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Uwaga! Strona {} zwraca błąd".format(site_name)
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()