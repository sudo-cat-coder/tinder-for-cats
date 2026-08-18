from django.apps import AppConfig
from django.core.signals import setting_changed

def callback(sender,**kwargs):
    print("Settings changed!")


class UserConfig(AppConfig):
    name = 'tinder_for_cats.user'

    def ready(self):
        setting_changed.connect(callback)
        
