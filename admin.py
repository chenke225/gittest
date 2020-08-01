from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ['title','author','visiting','created_time','modifyed_time']

class Entry1Admin(admin.ModelAdmin):
    list_display = ['title','author','visiting','created_time','modifyed_time']


admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Entry,EntryAdmin)
admin.site.register(models.Entry1, Entry1Admin)
admin.site.register(models.CustomData)
admin.site.register(models.CustomDataMonth)

