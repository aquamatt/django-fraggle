"Django admin registration and configuration"

from django.contrib import admin

from fraggle.models import Fragment

class FragmentOptions(admin.ModelAdmin):
    "Provides a more useful admin interface that the django default"
    search_fields = ['title', 'content']
    list_display = ('id', 'title', '_templatetag')
    ordering = ['id']
    fieldsets = (
        (None,
            {'fields':('title','content', 'use_textile')}
        ),
        ('Hidden',
            {
                'fields':('html',),
                'classes':('collapse',),                
            }
        ),
    )
    class Media:
        "Load styles and javascript for admin"
        css = { 
        'all': (
				'/static/css/admin.css',
                ) 
        }
try:
    admin.site.register(Fragment, FragmentOptions)
except admin.sites.AlreadyRegistered:
    pass
