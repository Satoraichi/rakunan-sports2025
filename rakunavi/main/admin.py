from django.contrib import admin
from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('session', 'number', 'name')
    list_filter = ('session',)
    search_fields = ('name',)
