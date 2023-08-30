import smtplib
from email.mime.text import MIMEText
from env import EMAIL

class Send_Email:
  
  def __init__(self, mail, index,contents):
    self.mail = mail
    self.index = index
    self.contents = contents
    
    print("Ready to Send Email")
      
    smtp = smtplib.SMTP(EMAIL.SMTP, EMAIL.PORT)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL.ACCOUNT, EMAIL.PASSWORD)

    msg = MIMEText(index)
    msg['Subject'] = contents

    smtp.sendmail(EMAIL.ACCOUNT, mail, msg.as_string())
    
    print("Successfully Sent Email")

    smtp.quit()
        
