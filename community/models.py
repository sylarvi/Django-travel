from django.db import models


# Create your models here.

#商品信息表
from user.models import UserProfile


class CommodityInfo(models.Model):
    commodityname = models.CharField('商品名称', max_length=30)
    price = models.DecimalField('商品价格', max_digits=8,decimal_places=2)
    image = models.ImageField('商品图片', upload_to='commodity/')
    user=models.ManyToManyField(UserProfile)
    num=models.IntegerField('商品数量')

