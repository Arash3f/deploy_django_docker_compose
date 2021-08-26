from django.contrib import admin
from image_test import models

@admin.register(models.Image)
class Image(admin.ModelAdmin):
    fields = ['image']