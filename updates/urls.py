from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^edit/profile$',views.edit_profile,name='edit-profile'),

    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),



]
