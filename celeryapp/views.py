from django.shortcuts import render
from django.http import HttpResponse
from .task import *
from .helper import *
from .forms import FileUploadForm
import pickle
from django.conf import settings
# Create your views here.



def index(request):
    shared_with_celery.delay()
    sleepy.delay(10)
    multiply.delay(10,50)
    return HttpResponse('<h1>Hai,this from celery</h1>')


def uploadfile(request):
    form=FileUploadForm()
    if request.method=='POST':
        data=request.FILES['file_upload']
        form=FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        filepath=f'{settings.MEDIA_ROOT}/documents/{data}'
        savedata.delay(filepath)
    return render(request,'upload.html',{'form':form})