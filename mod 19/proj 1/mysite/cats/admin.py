from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Breed)
admin.site.register(models.Cat)