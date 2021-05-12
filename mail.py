import RPi.GPIO as GPIO
import time
 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

GPIO.setmode(GPIO.BCM) 

IRsensor =  21
GPIO.setup(IRsensor, GPIO.IN)
 
fromaddr = ""    #Enter the sendor Email ID
toaddr = ""      #Enter the receiver Email ID 
 
mail = MIMEMultipart()
 
mail['From'] = fromaddr
mail['To'] = toaddr
mail['Subject'] = "Door Status"
body = "Please find the Door status "
 
 
def sendMail():
    mail.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Your password here")    #Enter the password of sensor email id
    text = "Door Open"
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
 

 
while (True):
    if GPIO.input(IRsensor):
        sendMail()
    else:
        time.sleep(0.01)
