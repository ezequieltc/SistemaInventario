from django.contrib import admin
from . import models

# Register your models here.


class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')


admin.site.register(models.Item)
admin.site.register(models.Lista)
admin.site.register(models.Venta, RatingAdmin)
admin.site.register(models.IngresoPedido)
