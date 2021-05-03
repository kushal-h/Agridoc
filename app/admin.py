from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Predictions)
class PredictionModel(admin.ModelAdmin):
    list_display = ['id','image_path','prediction']
    list_filter = ['prediction']
    icon_name = 'mms perm_identity compare'