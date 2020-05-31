from django.db import models

# Create your models here.

#
from user.models import UserProfile

#文章、攻略表
class IntroductionInfo(models.Model):
    #外键,用户表id
    userid=models.ForeignKey(UserProfile)
    shortinfo=models.CharField('文章简介',max_length=30)
    title=models.CharField('文章标题',max_length=30)
    info=models.TextField('文章内容')

#文章关键字表,与上表是一对一关系
class IntroductionKeyWord(models.Model):
    #外键,关联文章、攻略表
    titleid=models.ForeignKey(IntroductionInfo)
    keywords=models.CharField('文章关键字列表',max_length=50)


