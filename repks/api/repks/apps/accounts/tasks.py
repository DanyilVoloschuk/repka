from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_mail_task(sender='danyilvoloshchuk@gmail.com', all_recipients=None,
                   text=''):
    if all_recipients is None:
        all_recipients = ['danyilvoloschuk@gmail.com']

    email = EmailMessage('Subject', text, sender, all_recipients, )
    email.send()
