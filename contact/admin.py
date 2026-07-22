from django.contrib import admin
from contact.models import Contact
from contact.models import Category
# Register your models here.

@admin.register(Contact) #adiciona o model no admin do django
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = 'id',
    # list_filter = 'create_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone',

@admin.register(Category) #adiciona o model no admin do django
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',
    
   