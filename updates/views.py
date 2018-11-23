from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Business,NeighborHood,Userprofile
from .forms import NewProfileForm





#Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    businesses=Business.get_all_businesses()
    neighborhoods=NeighborHood.get_all_neighborhoods()


    return render(request,'index.html',{"businesses":businesses,"neighborhoods":neighborhoods})

def profile(request):
    current_user=request.user
    userprofile = Userprofile.objects.filter(user_name=current_user)

    if len(userprofile)<1:
        userprofile = "No profile"
    else:
        userprofile = Userprofile.objects.get(user_name=current_user)
    return render(request,'profile.html',{"userprofile":userprofile})

def neighborhood(request,neighborhood_id):
    neighborhood=NeighborHood.objects.get(id=neighborhood_id)

    return render(request,'neighborhood.html',{"neighborhood":neighborhood})


def edit_profile(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            userprofile=form.save(commit=False)
            userprofile.user_name = current_user
            userprofile.save()
        return redirect('profile')
    else:
        form=NewProfileForm()
    return render(request,'edit_profile.html',{"form":form})
