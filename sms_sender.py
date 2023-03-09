# sms_sender.py

from twilio.rest import Client

# Twilio 설정
account_sid = 'Twilio 계정
auth_token = 'Twilio 인증 토큰'
client = Client(account_sid, auth_token)
twilio_phone_number = '발신 전화번호'
my_phone_number = '수신 전화번호'

# 문자 발송
def send_sms(article_titles, summarized_texts):
    message = '\n'.join([f'{i+1}. {article_titles[i]} ({summarized_texts[i]})' for i in range(10)])
    message = client.messages.create(body=message, from_=twilio_phone_number, to=my_phone_number)
    
