import os
from twilio.rest import Client
from urllib.parse import urlencode
import env


class Sending(Client):

    print("successfully prepared message system")

    def __init__(self, account_sid=env.ACCOUNT_SID, auth_token=env.AUTH_TOKEN):

        # env 처리를 하려고 하였으나 AttributeError 발생 :  AttributeError: module 'env' has no attribute 'ACCOUNT_SID'
        super().__init__(account_sid, auth_token)

    def create_message(self, sending_message, to, from_=env.CALL_FROM):
        message = self.messages.create(
            body=sending_message,
            from_=from_,
            to=to
        )
        print(f"전송 완료: {message.sid}")
