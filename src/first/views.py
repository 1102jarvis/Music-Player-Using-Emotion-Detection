from django.shortcuts import render
from .forms import ImageForm
from django.conf import settings
from models.test import detect_emotion
import os
# Create your views here.
def home_screen(request):
  # print(request.headers)
  form = ImageForm(request.POST,request.FILES)
  return render(request,'index.html',{'form':form})

def get_emotion(request):
  if request.method == 'POST':
    form = ImageForm(request.POST,request.FILES)
    if form.is_valid():
      uploaded_img = form.save()
      imgUrl = uploaded_img.image.url
      imgPath = imgUrl.lstrip('/')
      emotion = detect_emotion(imgPath)
      if emotion != '':
       return render(request,'second.html',{'form':form,'emotion':emotion})
      else:
        form = ImageForm()
        return render(request,'second.html',{'form':form})  
    else:
      form = ImageForm()
      return render(request,'index.html',{'form':form})
    
  