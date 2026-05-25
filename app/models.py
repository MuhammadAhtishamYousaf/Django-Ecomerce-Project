from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
# Create your models here.

class SignupModel(models.Model):
    name = models.CharField(error_messages={'required':"Name is required"})
    username = models.CharField()
    email = models.EmailField()
    password=models.CharField(max_length=100)


    def __str__(self):
        return  f'{self.id} - {self.name} - {self.username} - {self.email} - {self.password}'



class AppModel(models.Model):
    p_name = models.CharField(max_length=50)
    p_desc = models.TextField(max_length=100)
    p_price = models.FloatField(max_length=50)
    p_image = models.FileField(upload_to='products/',null = True, default=None)


class BlogModel(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_desc = HTMLField()
    blog_image = models.FileField(upload_to='blogs/', null = True, default=None,blank=True)
    blog_slug = AutoSlugField(populate_from = 'blog_title', unique=True, null = True, default=None)