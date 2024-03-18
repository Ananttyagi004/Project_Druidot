from django.shortcuts import render
from .forms import PersonForm
import cv2
camera = cv2.VideoCapture(0)
# Create your views here.
def register(request):
    if request.method=='POST':
        forms=PersonForm(request.POST)
        if forms.is_valid():
            forms.save()
    forms=PersonForm()
    return render(request,'app/forms.html',{'forms':forms})

#def login(request):

            