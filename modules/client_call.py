import os
from twilio.rest import Client
from urllib.parse import urlencode
import env


class Calling(Client):

    # Use the Twilio-provided site for the TwiML response. Please Do not Modify
    URL = "https://twimlets.com/message?"

    def __init__(self, account_sid=env.ACCOUNT_SID, auth_token=env.AUTH_TOKEN):

        super().__init__(account_sid, auth_token)

    def create_call(self, sending_message, to, from_=env.CALL_FROM):
        call = self.calls.create(to=to,
                                 from_=from_,
                                 url=Calling.URL + urlencode({'Message': sending_message}))
        print(f"통화 완료: {call.sid}")
