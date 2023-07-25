'''
import os
from twilio.rest import Client
from urllib.parse import urlencode
import env


class sending:
  print("successfully prepared message system")
  
  #env 처리를 하려고 하였으나 AttributeError 발생 :  AttributeError: module 'env' has no attribute 'ACCOUNT_SID'
  sending_message = "안녕하세요! 오늘의 건강은 어떠신지요?"
  account_sid = "AC5f6ea393a0ed9c693dc1a6e375f1fc16"
  auth_token = "329bb3f529ff679ced275bd02a07cd42"
  client = Client(account_sid, auth_token)
  
  message = client.messages.create(
    body=sending_message,
    from_='+14068047188',
    to = "+821020359827"
  )
  print(message.sid)
  
  





'''