import os
from email.message import EmailMessage
import ssl
import smtplib

email_emisor = 'pruebaautomatizacionemails@gmail.com'
email_password = "hquw jsca rrym lwas"

email_receptor ='danyjr@outlook.es'

subject ='Prueba'
emailBody = """
            Que bueno soy
            PD. El correo se envio 
            """

em = EmailMessage()
em['From']=email_emisor
em['To']=email_receptor
em['Subject'] = subject
em.set_content(emailBody)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_emisor, email_password)
  smtp.sendmail(email_emisor, email_receptor, em.as_string())
