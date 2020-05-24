from django.contrib import admin

# Register your models here.
from seller.models import Type, Goods, GoodsImage


class GoodsAdmin(admin.ModelAdmin):
    list_display = ("goods_num", "goods_name", "goods_oprice", "goods_xprice")


class GoodsImageAdmin(admin.ModelAdmin):
    list_display = ("image_address", "goods",)


admin.site.register(Type)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsImage, GoodsImageAdmin)
