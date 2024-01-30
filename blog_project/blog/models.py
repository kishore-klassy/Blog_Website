from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.IntegerField(default=0)
class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name="Post Title",null=True,blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name="Author Name")
    content = models.TextField(verbose_name="Post Content",null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now,verbose_name="Post Created Date")
    post_image = models.ImageField(upload_to='media/',null=True, blank=True)
    def __str__(self):
        return f" {self.title} - {self.author.username} "
