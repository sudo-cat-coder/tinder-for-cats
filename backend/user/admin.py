from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    fields = [ 'user_id' , 'name' , 'gender']


class UserAdmin(admin.ModelAdmin):
    pass




admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)