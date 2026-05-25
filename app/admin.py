from django.contrib import admin
from app.models import AppModel, BlogModel, SignupModel

# Register your models here.
class AppAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'p_desc', 'p_price','p_image')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_desc','blog_image')

class SignupUsers(admin.ModelAdmin):
    list_display = ('name','username','email','password')

admin.site.register(SignupModel,SignupUsers)
admin.site.register(BlogModel,BlogAdmin)
admin.site.register(AppModel,AppAdmin)


