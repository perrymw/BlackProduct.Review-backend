from django.contrib import admin
from blackproduct_app import models
# Register your models here.


admin.site.register(models.BusinessAddress)
admin.site.register(models.Business)
admin.site.register(models.BPRUser)
admin.site.register(models.Reviews)
admin.site.register(models.Product)
admin.site.register(models.Comment)
