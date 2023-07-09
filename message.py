import os
from twilio.rest import Client

client_example = ["장원준",1,"+821020359827","서울특별시 중랑구 동일로 92길"]
phone_num_server = ["+14068047188",0,0,0,0,0] # Settign 6 Server for Check Information
send_target = [0,0,0,0]
if client_example[1]==1:
   sent_message = str(client_example[0])+" 안녕하세요! 다음의 정보를 확인해주세요! "+str(client_example[3])


account_sid = "AC5f6ea393a0ed9c693dc1a6e375f1fc16"
auth_token = "60f6f46a313a6651c54a12c59a5b5e84"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body=sent_message,
  from_="+14068047188",
  to=client_example[2]
)
print(message.sid)

