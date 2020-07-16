from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.Listing)
admin.site.register(models.Sale)
admin.site.register(models.PaymentsStore)
admin.site.register(models.TempStorage)


@admin.register(models.Listing)
class DeviceAdmin(admin.ModelAdmin):
  search_fields = ["seller_user","freefire_id","estimated_price","price","is_published"]
  list_display = ("seller_user","freefire_id","level","estimated_price","price","is_published","is_sold")
  list_filter = ("price","is_published")
  list_editable = ("is_published","is_sold")


admin.site.site_header = 'FreeFireHub'
