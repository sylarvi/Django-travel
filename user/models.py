from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
#create by julun
#date:2020/05/31
#用户表
USERTYPE=(
    (1,'普通用户'),
    (2,'酒店'),
    (3,'旅游景点'),
)
class UserProfile(AbstractUser):
    #用户属性
    usertype=models.IntegerField('用户属性',choices=USERTYPE,default=1)
