from django.contrib import admin
from .models import Project, Review, Tag

'''
    Inregistrarea in baza de date oferita de Django a acestor clase
'''
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
