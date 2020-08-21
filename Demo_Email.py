'''
Step1: Crearting an object
Step2: Accessing Login credential
Step4 : Some kind of Maessage
'''

import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)


s.starttls()
s.login("SenderEmail","Password")
Message = " Thanks for Showing interest "

s.sendmail("SenderEmail", "Receiver",Message)
print("Your mail has been Shared Successfully")
s.quit()