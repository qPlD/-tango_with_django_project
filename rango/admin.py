from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)



class page(admin.ModelAdmin):
    
    #fields = ['TITLE','CATEGORY','URL']
    fieldsets = [
        (None, {'fields': ['TITLE']}),
        (None, {'fields': ['CATEGORY']}),
        (None, {'fields': ['URL']}),
        ]
    
    list_display = ('title','category','url')

admin.site.register(Page,page)
#Adding further classes which may be created in the future is as simple as adding another
#call to the admin.site.register() method
