from django.shortcuts import render
from FaceReg import faceRegProg
import datetime,pytz

d={
    'Date':str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).year)+'-'+str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).month)+'-'+str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).day),
    'Time':str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).hour)+':'+str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')).minute),
    'result':faceRegProg()
}

def home(request):
    return render(request, 'faceReg/home.html', d)
def media(request):
    return render(request, 'faceReg/media.html')
def radio(request):
    return render(request, 'faceReg/radio.html')