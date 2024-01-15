from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from models import test
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
      emotion = test(imgUrl)
      return render(request,'second.html',{'form':form,'emotion':emotion})
    else:
      form = ImageForm()
      return render(request,'index.html',{'form':form})
    
  