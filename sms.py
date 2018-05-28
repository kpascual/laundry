from twilio.rest import Client


TWILIO_ACCOUNT_SID = '<account_sid>'
TWILIO_AUTH_TOKEN = '<auth_token>'
TWILIO_PHONE_NUMBER = '+<from_phone_number>'
MY_PHONE_NUMBER = '+<to_phone_number>'



def textMe(message_body):

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(to=MY_PHONE_NUMBER, from_=TWILIO_PHONE_NUMBER, body=message_body)

