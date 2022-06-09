from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    carbs=models.FloatField()
    protien=models.FloatField()
    fats=models.FloatField()
    calorie=models.IntegerField()
    food_img=models.CharField(max_length=500,default="https://kimerahome.com/wp-content/uploads/2020/08/Product-Placeholder.jpg")

class Consume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed=models.ForeignKey(Food,on_delete=models.CASCADE)

class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="profile_pictures")
    def __str__(self):
        return self.caption



