__author__ = 'robertb'

import sys
from django.conf import settings
from django.core.management.base import BaseCommand

from notifications.utils import get_mailchimp_api
from notifications.models import Recipient
import mailchimp


# class Email(object):
#     email = ''
#
#     def __init__(self, email):
#         self.email = email


class Command(BaseCommand):
    help = 'executes a batch update to mailchimp with all current active users'

    def execute_batch_update(self):
        recipients = Recipient.objects.all()
        recipients = set(recipients)
        recipients_list = []
        batch = []
        for r in recipients:
            if r.user.email not in recipients_list:
                recipients_list.append(str(r.user.email))
            else:
                pass
        for email in recipients_list:
            # recipient = Email(email)
            batch.append({'email': email})

        for obj in batch:
            print obj['email']

        mailchip_client = get_mailchimp_api()
        results = mailchip_client.lists.batch_subscribe(settings.LIST_ID, batch, double_optin=False, update_existing=True)

        print results

    def handle(self, *args, **options):
        self.execute_batch_update()