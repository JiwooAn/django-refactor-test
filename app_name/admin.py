from django.contrib import admin
from .models import Check


# Register your models here.
class CheckAdmin(admin.ModelAdmin):
    abc = ['abc']
    xyz = ['xyz']


admin.site.register(Check, CheckAdmin)