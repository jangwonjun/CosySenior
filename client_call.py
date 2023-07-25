'''
import os
from twilio.rest import Client
from urllib.parse import urlencode
import env

class calling:
    account_sid = "AC5f6ea393a0ed9c693dc1a6e375f1fc16"
    auth_token = "329bb3f529ff679ced275bd02a07cd42"
    from_number = '+14068047188'
    to_number = "+821020359827"
    # Use the Twilio-provided site for the TwiML response. Please Do not Modify 
    url = "https://twimlets.com/message?"
    message = "이것은 테스트 입니다."
    client = Client(account_sid, auth_token)
    call = client.calls.create(to=to_number,
                              from_=from_number,
                              url=url + urlencode({'Message': message}))
    print(call.sid)
'''