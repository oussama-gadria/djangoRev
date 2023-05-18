from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    actions=[]
    inlines=[]
    list_display=('title','category','state') 
    ordering=('title',)
    list_filter=('state','category')
    search_fields=[ 
        'title',
        'category'
    ]
    list_per_page=5
    readonly_fields=('created_at','updated_at')
    fieldsets=(
        (
            'STATE',
            { 
                
            }
        )
    )
    




admin.site.register(Event,EventAdmin)
admin.site.register(Participation)
# Register your models here.
