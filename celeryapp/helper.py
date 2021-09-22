
from django.core.mail import send_mail


def send_mail_without_celery():
    send_mail('Csv data upload successfully','Now you can enjoy','javashrm@gmail.com',['pranav.bluethink@gmail.com'],fail_silently=False)
    return None