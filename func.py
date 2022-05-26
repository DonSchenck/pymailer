from parliament import Context, event
import yagmail
import os
import json

@event
def main(context: Context):
    
     # Get credentials from environment variables, which will be
     # stored in an OpenShift secret
    sender_email_address  = os.environ['SENDER_EMAIL_ADDRESS']
    sender_email_password = os.environ['SENDER_EMAIL_PASSWORD']

    emaildata = json.loads(context.cloud_event.data)
    receiver  = emaildata['recipient']
    body      = "Hello there from the PyMailer Function as a Service, running in OpenShift using OpenShift Serverless Functions."

    yag = yagmail.SMTP(sender_email_address,sender_email_password)

    yag.send(
        to=receiver,
        subject=emaildata['subject'],
        contents=body, 
    )

    return { "message": receiver }
