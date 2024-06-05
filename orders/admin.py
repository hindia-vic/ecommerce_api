from django.contrib import admin

from . models import Orders
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=['customer','size','status','quantity','created_at']
    list_filter=['created_at','status','size']
admin.site.register(Orders,OrderAdmin)
