from django.contrib import admin
from First_App .models import Musician, Album

# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)