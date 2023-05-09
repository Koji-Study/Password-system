from django.contrib import admin

# Register your models here.
from djangoapp.models import password

class passwordmanager(admin.ModelAdmin):
    list_display=['key','value','desc']
    list_display_links=['key']
    search_fields=['key']

admin.site.index_title="Hello~"
admin.site.site_title="Password"
admin.site.site_header="Password" 
admin.site.register(password, passwordmanager)
