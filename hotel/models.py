from django.db import models

# Create your models here.
# 酒店模块
from user.models import UserProfile


class HotelInfo(models.Model):
    hotelname = models.CharField('酒店名称', max_length=30)
    # 外键,关联用户信息表
    userid = models.ForeignKey(UserProfile)
    # 地理位置
    locate = models.CharField('地理位置', max_length=30)
    price = models.DecimalField('每晚价格', max_digits=8,decimal_places=2)


# 酒店关键字列表
class HotelKeyWords(models.Model):
    hotelid = models.ForeignKey(HotelInfo)
    hotelkeywords = models.CharField('关键字',max_length=30)
