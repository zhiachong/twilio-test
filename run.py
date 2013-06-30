from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
 

@app.route("/", methods=['GET', 'POST'])
def hello_monkey(): 
    #todo
    #get phone number & msg from incoming msg
    #know which phone number to send to by querying the database
    #finally, send the msg
    account_sid = "ACc34c6db115eb6f7fa3ffb5efb10f2ec3"
    auth_token = "07ec4e439d0025ae71b28509cc801857"

    from_phone = request.values.get('From', None)
    #to_phone = request.values.get('To', None)
    to_phone = "+17164796637"
    msg_body = request.values.get('Body', None)
    #resp = twilio.twiml.Response()

    client = TwilioRestClient(account_sid, auth_token)
    mesasge = client.sms.messages.create(to=to_phone, from_=from_phone, body=msg_body)
    


if __name__ == "__main__":
    app.run(debug=True)
