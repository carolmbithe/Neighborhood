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

    def update_neighborhood(self):
        self.neighborhood_image=neighborhood_image
        self.name=name
        self.location=location
        self.occupants_count=occupants_count
        self.save()


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
        # NeighborHood.objects.filter(id=userprofile_id).update(neighborhood="neighborhood_id")

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


    def update_business(self):
        self.business_image=business_image
        self.business_name=business_name
        self.user=location
        self.neighborhood=neighborhood
        self.email=email
        self.save()

    @classmethod
    def filter_by_neighborhood(cls,neighborhood_id):
        businesses=cls.objects.filter(id=neighborhood_id)
        return businesses


    @classmethod
    def find_business_by_id(cls,business_id):
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
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE,blank=True,null=True)
    post=models.TextField()

    def __str__(self):
        return self.title

    @classmethod
    def get_all_posts(cls):
        posts=cls.objects.all()
        return posts
    def save_post(self):
        self.save()
    def delete_post(self):
        self.delete()

class HealthCenter(models.Model):
    name = models.CharField(max_length = 50)
    location=models.CharField(max_length =50)
    contact=models.CharField(max_length=40)

    @classmethod
    def get_all_health(cls):
        health=cls.objects.all()
        return health

class PoliceCenters(models.Model):
    name = models.CharField(max_length = 50)
    location=models.CharField(max_length =50)
    contact=models.CharField(max_length=40)

    @classmethod
    def get_all_police(cls):
        police=cls.objects.all()
        return police



class Comment(models.Model):
    post = models.ForeignKey(Post,blank=True, on_delete=models.CASCADE,null=True,related_name='comment')
    commenter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    comment=models.TextField(max_length =30)



    def delete_comment(self):
        self.delete()

    def save_comment(self):
        self.save()

    @classmethod
    def get_comments(cls):
        comments=cls.objects.all()
        return comments

    @classmethod
    def get_comments_by_post_id(cls,post_id):
        comments=cls.objects.filter(id=post_id)
        return comments


class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
