from twilio.rest import TwilioRestClient
 
def sendMessage(messageBody, to_phone):
    from_phone = "+12067456226"
    account_sid = "ACc34c6db115eb6f7fa3ffb5efb10f2ec3"
    auth_token = "07ec4e439d0025ae71b28509cc801857"
    client = TwilioRestClient(account_sid, auth_token)
     
    message = client.sms.messages.create(to=to_phone, from_=from_phone,
                                         body=messageBody)