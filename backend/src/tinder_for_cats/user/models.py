from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'),unique=True)
    username = None
    password = models.CharField(max_length=255, verbose_name='password')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class User (abstractBaseUser):
#     email = models.EmailField(_('email address'),unique=True)
#     username = models.CharField(max_length=255 , unique=True)
#     password = models.CharField(max_length=255 , verbose_name='password')
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


class Profile(models.Model):

    FEMALE = 'FEMALE'
    MALE = 'MALE'
    CUSTOM = 'CUSTOM'
    NONE = 'NONE'

    GENDER = [
    (FEMALE, "Female"),
    (MALE, "Male"),
    (NONE, "Prefer not to say"),
    ]

    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/' )
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255 , unique=True)
    bio = models.TextField(blank=True)
    gender = models.CharField(choices=GENDER , default=NONE)

    def __str__(self):
        return str(self.user_id.pk)

@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.get_or_create(user_id=instance)
