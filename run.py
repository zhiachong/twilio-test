from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
 
account_sid = "ACc34c6db115eb6f7fa3ffb5efb10f2ec3"
auth_token = "07ec4e439d0025ae71b28509cc801857"
@app.route("/", methods=['GET', 'POST'])
def hello_monkey(): 
    #todo
    #get phone number & msg from incoming msg
    #know which phone number to send to by querying the database
    #finally, send the msg

    from_phone = request.values.get('From', None)
    to_phone = request.values.get('To', None)
    msg_body = request.values.get('Body', None)
    resp = twilio.twiml.Response()

    
    client = TwilioRestClient(account_sid, auth_token)
    mesage = client.sms.messages.create(to=to_phone, from_=from_phone, body=msg_body)
    


    #this is for sms
    #resp.sms("Hello, Mobile Monkey")
    #return  str(resp)

    #this is for voice
    #resp.say("hello boy")
    #return str(resp)
    

    #message = client.sms.messages.create(to="+17164796637", from_="+12067456226",
    #                                     body="Hello there!")
        


if __name__ == "__main__":
    app.run(debug=True)
