from django.db import models

# Create your models here.
#create by julun
#date:2020/05/30

#商家信息表
from user.models import UserProfile


class StoreInfo(models.Model):
    commodityname=models.CharField("商家名称",max_length=30)
    #外键 关联用户信息表 1对多关系
    userid=models.ForeignKey(UserProfile)
    price=models.DecimalField("商品价格",max_digits=8,decimal_places=2)
    image=models.ImageField(upload_to='store/')

class StoreDetails(models.Model):
    #商品信息表id,与商品信息表是一对一关系
    commodityid=models.OneToOneField(StoreInfo)
    #这里指的是商品详情,这里的商品指的是酒店发布的酒店信息,景区发布的
    info=models.TextField('商品详情')