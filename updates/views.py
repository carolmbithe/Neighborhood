from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Business,NeighborHood,Userprofile,Post
from .forms import NewProfileForm,NewNeighborhoodForm,UpdateForm,NewPostForm,NewBusinessForm





#Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    businesses=Business.get_all_businesses()
    neighborhoods=NeighborHood.get_all_neighborhoods()
    posts=Post.get_all_posts()


    return render(request,'index.html',{"businesses":businesses,"neighborhoods":neighborhoods,"posts":posts})

def post(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.owner = current_user
            post.save()
        return redirect('index')
    else:
        form=NewPostForm()
    return render(request,'post.html',{"form":form})

def business(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewBusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business=form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('index')
    else:
        form=NewBusinessForm()
    return render(request,'business.html',{"form":form})


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


def update_neighborhood(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewNeighborhoodForm(request.POST,request.FILES)
        if form.is_valid():
            userprofile=form.save(commit=False)
            userprofile.user_name = current_user
            userprofile.save()
        return redirect('update-profile')
    else:
        form=NewNeighborhoodForm()
    return render(request,'update_neighborhood.html',{"form":form})

def update_profile(request):
    current_user=request.user
    # print(current_user)
    if request.method == 'POST':
        form =UpdateForm(request.POST,request.FILES)
        if form.is_valid():
            # update=form.save(commit=False)

            userprofile=form.save(commit=False)
            # userprofile=Userprofile.objects.get(pk=userprofile_id)
            # form =UpdateForm(request.POST,instance=userprofile)
            # update.user_name = current_user
            update.save()
        return redirect('profile')
    # elif Userprofile.objects.get(user_name=current_user):
    # #     profile= Userprofile.objects.get(user_name=current_user)
    # #     form = NewProfileForm(instance=profile)
    else:
        form=UpdateForm()
    return render(request,'update_profile.html',{"form":form})



def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_business_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def businessdetails(request,business_id):

    business=Business.objects.get(id=business_id)

    return render(request,"businessdetails.html",{"business":business})
