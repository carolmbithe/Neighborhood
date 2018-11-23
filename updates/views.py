from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Business,NeighborHood,User




#Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    businesses=Business.get_all_businesses()
    neighborhoods=NeighborHood.get_all_neighborhoods()


    return render(request,'index.html',{"businesses":businesses,"neighborhoods":neighborhoods})

def profile(request):
    current_user=request.user

    return render(request,'profile.html')
