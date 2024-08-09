from django.contrib import admin
from .models import Author,Books,Publisher,User

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Publisher)
admin.site.register(User)
