from .models import Business,NeighborHood,Userprofile,Post
from django import forms


class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        exclude=['user_name']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['user']

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        exclude=["user_name","email"]

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model=NeighborHood
        fields=['neighborhood_image','name','location','count']

class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['owner']
