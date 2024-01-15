from django import forms
from .models import Face_Image

class ImageForm(forms.ModelForm):
  class Meta:
    model = Face_Image
    fields = ('image',)
    widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*', 'capture': 'environment'}),
        }
    
    
