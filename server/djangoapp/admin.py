from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.



# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarMake
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['title']


# CarMakeAdmin class with CarModelInline
class CarModelAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)