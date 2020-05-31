from django.db import models

# Create your models here.
#景点表
# 文章、攻略表
from user.models import UserProfile


class TourPlace(models.Model):
    # 外键,用户表id
    userid = models.ForeignKey(UserProfile)
    placename = models.CharField('景区名称', max_length=30)
    price = models.DecimalField('票价',max_digits=8,decimal_places=2)
    info = models.TextField('景区简介')
    image=models.ImageField(upload_to='tour/')
    locate=models.CharField('地理位置',max_length=30)
# 文章关键字表,与上表是一对一关系
class PlaceKeyWord(models.Model):
    # 外键,关联文章、攻略表
    titleid = models.ForeignKey(TourPlace)
    keywords = models.CharField('景区关键字列表', max_length=50)
