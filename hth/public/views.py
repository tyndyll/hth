import os

from django.shortcuts import render
from twilio.util import TwilioCapability

def home(request):
    capability = TwilioCapability(os.environ['ACCOUNT_SID'], os.environ['AUTH_TOKEN'])
    capability.allow_client_outgoing(os.environ['APPLICATION_SID'])
    return render(request, 'public/home_page.html', {'twilio_token': capability.generate()})
