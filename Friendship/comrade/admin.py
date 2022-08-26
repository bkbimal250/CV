from django.contrib import admin
from  comrade.models import Members

# Register your models here.


class memb_Admin(admin.ModelAdmin):
    
    list_display=('firstname','lastname')
    
admin.site.register(Members,memb_Admin)
    

