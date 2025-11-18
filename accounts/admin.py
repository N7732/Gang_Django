from django.contrib import admin
from .models import CustomUser, Vendor  # <-- use CustomUser, not Custom_user

# Register CustomUser
admin.site.register(CustomUser)

# Register Vendor
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("company_name", "status")  # <-- comma fixes the tuple
    list_filter = ("status",)
