from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Goods(models.Model):
    goods_num = models.CharField(max_length=32)  # 编号
    goods_name = models.CharField(max_length=32)  # 名称
    goods_oprice = models.CharField(max_length=32)  # 原价
    goods_xprice = models.CharField(max_length=32)  # 现价
    goods_kucun = models.CharField(max_length=32)  # 库存
    goods_desc = models.CharField(max_length=32)  # 简单描述
    goods_detail = models.CharField(max_length=128)  # 详情
    type = models.ForeignKey(to=Type, on_delete=models.CASCADE)  # 商品类型和商品关系一对多

    def __str__(self):
        return self.goods_name


class GoodsImage(models.Model):
    # upload_to: 表示上传文件的具体目录  static/goodsimage
    image_address = models.ImageField(upload_to='goodsimage')
    goods = models.ForeignKey(to=Goods, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image_address)
