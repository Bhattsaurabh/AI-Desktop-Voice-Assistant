import smtplib
from credentials import myemailid, password

def sendMail(emailid, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)  #hostname and port number
    server.ehlo()            #client sends this command to the SMTP server to identify itself and initiate the SMTP conversation
    server.starttls()      #start connection to SMTP server in TLS mode
    server.login(myemailid, password)   #login
    server.sendmail(myemailid, emailid, content)
    server.close()