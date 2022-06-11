from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class ToDoList(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Item(models.Model):
    todolist=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    complete=models.BooleanField()

    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
