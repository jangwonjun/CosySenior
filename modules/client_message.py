import os
from twilio.rest import Client
from urllib.parse import urlencode
from env import CALLS_ENUM


class Sending(Client):
    # schedule.every().day.at(time_value).do(__init__)
    print("successfully prepared message system")

    def __init__(self, account_sid=CALLS_ENUM.ACCOUNT_SID, auth_token=CALLS_ENUM.AUTH_TOKEN):

        super().__init__(account_sid, auth_token)

    def create_message(self, sending_message, to, from_=CALLS_ENUM.CALL_FROM):
        message = self.messages.create(
            body=sending_message,
            from_=from_,
            to=to
        )
        print(f"전송 완료: {message.sid}")

