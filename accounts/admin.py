from django.contrib import admin
from .models import Custom_user, Vendor


# Register your models here.
admin.site.register(Custom_user)
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("company_name" "status")
    list_filter = ("status",)
