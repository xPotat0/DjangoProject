from django.contrib import admin
from .models import *

# Register your models here.


class IndexAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'list')
    list_display_links = ('title', 'text', 'list')
    search_fields = ('title', 'list')


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'year')
    list_display_links = ('name', 'amount')
    search_fields = ('name', 'year')


class DemandAdmin(admin.ModelAdmin):
    list_display = ('year', 'salary_amount', 'type')
    list_display_links = ('year', 'salary_amount', 'type')
    search_fields = ('year', 'type')


class GeographyAdmin(admin.ModelAdmin):
    list_display = ('city', 'salary_amount', 'type')
    list_display_links = ('city', 'salary_amount', 'type')
    search_fields = ('city', 'type')


admin.site.register(Index, IndexAdmin)
admin.site.register(Geography, GeographyAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Demand, DemandAdmin)