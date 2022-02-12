from django.contrib import admin
from .models import Category, FoodCard, Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'sent_at')

admin.site.register(Contact, ContactAdmin)    
admin.site.register(FoodCard)
admin.site.register(Category)