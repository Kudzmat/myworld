from django.contrib import admin
from .models import PersonalProject

# Register your models here.
@admin.register(PersonalProject)
class PersonalProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    search_fields = ('name',)
    readonly_fields = ('date',)