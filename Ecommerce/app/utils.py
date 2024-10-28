from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from random import randint

def send_email_to_client(email):
    subject = 'Account Verification'
    code = randint(1,100000)
    message = f'Hi there, your email verification code for a password change is {code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return code