from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class NeighborHood(models.Model):
    name=models.CharField(max_length =400)
    location=models.CharField(max_length=40)
    count=models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.user

    def save_neighborhood(self):
        self.save()
    def delete_neighborhood(self):
        self.delete()

class User(models.Model):
    user_name = models.OneToOneField(User,null = True,on_delete=models.CASCADE,related_name = "profile")
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE)
    email=models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.user

    def save_user(self):
        self.save()
    def delete_user(self):
        self.delete()

class Business(models.Model):
    business_name=models.CharField(max_length =30)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighborhood=models.ForeignKey(NeighborHood,on_delete=models.CASCADE)
    email=models.EmailField(blank=True,null=True)

    def save_business(self):
        self.save()
    def delete_business(self):
        self.delete()
