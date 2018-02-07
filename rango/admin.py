from django.contrib import admin
from rango.models import Category, Page, UserProfile





class page(admin.ModelAdmin):
    
    #fields = ['TITLE','CATEGORY','URL']
    fieldsets = [
        (None, {'fields': ['TITLE']}),
        (None, {'fields': ['CATEGORY']}),
        (None, {'fields': ['URL']}),
        ]
    
    list_display = ('title','category','url')

class categ(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, categ)
admin.site.register(Page,page)
admin.site.register(UserProfile)
#Adding further classes which may be created in the future is as simple as adding another
#call to the admin.site.register() method
