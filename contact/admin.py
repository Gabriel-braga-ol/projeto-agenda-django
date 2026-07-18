from django.contrib import admin
from contact.models import Contact
# Register your models here.

@admin.register(Contact) #adiciona o model no admin do django
class ContactAdmin(admin.ModelAdmin):
    ...