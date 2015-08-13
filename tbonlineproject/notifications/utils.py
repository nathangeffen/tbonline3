__author__ = 'robertb'

import mailchimp
from django.conf import settings


def get_mailchimp_api():
    return mailchimp.Mailchimp(settings.MAILCHIMP_KEY) #your api key here
