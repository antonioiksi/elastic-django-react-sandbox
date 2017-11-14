from django.contrib import admin

# Register your models here.
from .models import Bin, BinItem


class BinAdmin (admin.ModelAdmin):
    list_display = ('user','name',)
    #ordering = ('-datetime','user')
    #list_filter = (
    #    ('ip'),('user'),('event'),
    #)

class BinItemAdmin (admin.ModelAdmin):
    list_display = ('bin','data','query','mapping',)


admin.site.register(Bin, BinAdmin)
admin.site.register(BinItem, BinItemAdmin)
