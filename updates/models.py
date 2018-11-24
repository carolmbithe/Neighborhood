from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class NeighborHood(models.Model):

    neighborhood_image=models.ImageField(upload_to='neighborhoods',null=True)
    name=models.CharField(max_length =40)
    location=models.CharField(max_length=40)
    occupants_count=models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

    def save_neighborhood(self):
        self.save()
    def delete_neighborhood(self):
        self.delete()

    # def update_neighborhood():


    def update_occupants(self,occupants_count):
        self.occupants_count=occupants_count
        self.save()


    @classmethod
    def find_neighborhood_by_id(cls,neighborhood_id):
        neighborhood=cls.objects.get(id=neighborhood_id)
        return neighborhood

    @classmethod
    def get_all_neighborhoods(cls):
        neighborhoods=cls.objects.all()
        return neighborhoods



class Userprofile(models.Model):

    profile_image=models.ImageField(upload_to='userprofiles',null=True)
    user_name=models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "user")
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)



    def save_userprofile(self):
        self.save()
    def delete_userprofile(self):
        self.delete()

    def update_neighborhood(self,neighborhood):
        self.neighborhood=neighborhood
        self.save()


class Business(models.Model):
    business_image=models.ImageField(upload_to='businesses',null=True)
    business_name=models.CharField(max_length =30)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)

    def save_business(self):
        self.save()
    def delete_business(self):
        self.delete()

    # def update_business(self):


    @classmethod
    def get_business_by_id(cls,business_id):
        business=cls.objects.get(id=business_id)
        return business


    @classmethod
    def get_all_businesses(cls):
        businesses=cls.objects.all()
        return businesses


    @classmethod
    def search_by_business_name(cls,search_term):
        businesses = cls.objects.filter(business_name__icontains=search_term)
        return businesses

class Post(models.Model):
    post_image=models.ImageField(upload_to='posts',null=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length =30)
    post=models.TextField()


    @classmethod
    def get_all_posts(cls):
        posts=cls.objects.all()
        return posts
    def save_post(self):
        self.save()
    def delete_post(self):
        self.delete()
