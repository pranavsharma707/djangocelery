from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import *
import csv
from .models import CarModels

# app=Celery('tasks',broker='amqp://guest:guest@localhost//')

@shared_task(name='sleppy')
def sleepy(duration):
    sleep(duration)
    return None


@shared_task(name='send_mail_with_celery')
def shared_with_celery():
    send_mail('Csv data upload successfully','Now you can enjoy','javashrm@gmail.com',['pranav.bluethink@gmail.com'],fail_silently=False)
    print('mail from celery')
    return None

@shared_task(name='multiple_two_numbers')
def multiply(x,y):
    data = x * y
    print("Multiplied Data---",data)

@shared_task(name='csvfiledatasave')
def savedata(filepath):
    # print('my filepath',filepath)
    with open(filepath,'r') as csvfile:
        csvreader=csv.DictReader(csvfile)
        for data in csvreader:
            carmodels=CarModels(id=data['id'],name=data['name'],
            active=data['active'],make_id=data['make_id'],
            created_at=data['created_at'],
            updated_at=data['updated_at'])
            carmodels.save()
        send_mail('Csv data upload successfully','Now you can enjoy',
        'javashrm@gmail.com',['pranav.bluethink@gmail.com'],fail_silently=False)
    return "Data Store Successfully"
                
    
# @shared_task(name='upload csv data')



