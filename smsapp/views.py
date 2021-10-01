from django.shortcuts import render,redirect
import os
from twilio.rest import Client
# Create your views here.
def homepageview(request):
    return render(request,"smsapp/homepage.html")


def sendSms(request):
    phoneNo = request.POST['phoneNo']
    message = request.POST['message']
    print(phoneNo,message)
    account_sid = '****'
    auth_token = '****'
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=message,
                        from_='3375484364',
                        to=phoneNo
                    )

    print(message.sid)
    return redirect(request.META['HTTP_REFERER'])