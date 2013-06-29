from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import smtplib
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey(): 
        server = smtplib.SMTP ("smtp.gmail.com", 587)
        server.starttls()
        server.login('zhiachong@gmail.com', 'chongzhiahwa')
        numberFormat = '17164796637' + '@tmomail.net'
        server.sendmail('123112312', numberFormat, 'damn')
        

if __name__ == "__main__":
    app.run(debug=True)
