from django.contrib import admin

# Register your models here.
from .models import Profile, Skill, Message

"""
    Aduauga aceste clase asa incat sa fie in baza de date a Django-ului
"""

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)
