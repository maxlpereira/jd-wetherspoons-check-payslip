import os
from twilio.rest import Client

def send():
        account_sid = "TWILIO SID"
        auth_token = "TWILIO TOKEN"
        client = Client(account_sid, auth_token)

        numbers_to_message = ['LIST OF PHONE NUMBERS TO SEND MESSAGE']
        message_body = "Payslip is AVALIABLE"
        for number in numbers_to_message:
                message = client.messages.create(
          	body = message_body,
          	from_="TWILIO'S PHONE NUMBER",
                to= number)
