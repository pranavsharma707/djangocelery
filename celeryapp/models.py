from django.db import models

# Create your models here.


class FileUpload(models.Model):
    file_upload=models.FileField(upload_to='documents')


class CarModels(models.Model):
    id=models.CharField(max_length=255,primary_key=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    active=models.CharField(max_length=10,null=True,blank=True)
    make_id=models.CharField(max_length=50,null=True,blank=True)
    created_at=models.DateTimeField(max_length=255,null=True,blank=True)
    updated_at=models.DateTimeField(max_length=255,null=True,blank=True)

