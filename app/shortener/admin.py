from django.contrib import admin
from .models import Urlentry, Leads

# Register your models here.
@admin.register(Urlentry)
class UrlentryAdmin(admin.ModelAdmin):
    fields = ['full_url', 'url_hash', 'owner', 'created_at']
    list_display = ('full_url', 'url_hash', 'owner', 'created_at')
    list_filter = ['created_at','owner', 'url_hash']
    list_per_page = 15
    date_hierarchy = 'created_at'
    ordering = ['url_hash']

@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    fields = ['urlentry', 'clicked_at', 'clicked_host', 'clicked_conf', 'clicked_ip']
    list_display = ('urlentry','clicked_at','clicked_host','clicked_conf','clicked_ip')
    list_filter = ['urlentry','clicked_at']
    list_per_page = 15
    date_hierarchy = 'clicked_at'
