

from django.contrib import admin
#from mysite.travel.models import Place
# Register your models here.


from .models import Place,List,Country

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')



admin.site.register(Place,PlaceAdmin)

admin.site.register(List)

admin.site.register(Country)



