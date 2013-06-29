from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    #resp = twilio.twiml.Response()
    #resp.sms("Hello, Mobile Monkey")
    #return str(resp)
    # Download the twilio-python library from http://twilio.com/docs/libraries

 
# Find these values at https://twilio.com/user/account
    account_sid = "AC39492bb1f7999a7d44f9809ed9b55f93"
    auth_token = "84a048734ff992a96cd50422c33e29dc"
    client = TwilioRestClient(account_sid, auth_token)
     
    message = client.sms.messages.create(to="+17164796637", from_="+12088164276",
                                         body="Hello crazy monkey!")
 
if __name__ == "__main__":
    app.run(debug=True)
