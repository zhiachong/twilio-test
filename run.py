from flask import Flask, request, redirect
from hungermob.app.main.models import MessageSession, UserProfile

from twilio.rest import TwilioRestClient
import twilio.twiml

app = Flask(__name__)
 

@app.route("/", methods=['GET', 'POST'])
def hello_monkey(): 
    #todo
    #get phone number & msg from incoming msg
    #know which phone number to send to by querying the database
    #finally, send the msg
    account_sid = "ACc34c6db115eb6f7fa3ffb5efb10f2ec3"
    auth_token = "07ec4e439d0025ae71b28509cc801857"

    incoming_msg_num = request.values.get('From', None)
    from_phone = "+12067456226"
    #now do a query on the database to pull out the conversation
    users = UserProfile.objects.filter(phone_number=incoming_msg_num)
    if (len(users) != 0):
        user_phone = users[0].phone_number

    msg_body = request.values.get('Body', None)
    msg_body += user_phone
    #use number associated with the msg sender to find whom to send to
    to_phone = "+12083051792"


    client = TwilioRestClient(account_sid, auth_token)
    message = client.sms.messages.create(to=to_phone, from_=from_phone, body=msg_body)

if __name__ == "__main__":
    app.run(debug=True)
