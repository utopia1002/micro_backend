from django.contrib import admin
from .models import Real_estate, Category, MyUser, Like
# Register your models here.
admin.site.register(Real_estate)
admin.site.register(Category)
admin.site.register(MyUser)
admin.site.register(Like)
