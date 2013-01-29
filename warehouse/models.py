# -*- coding: utf8 -*-
from django.db import models
import datetime
from django.contrib import admin
from system_avalibe.models import my_user
from system_avalibe.models import sp_type
from system_avalibe.models import sp_company
from system_avalibe.models import warehouse_position
# Create your models here.

class warehouse (models.Model):
    sp_id=models.CharField(max_length=16,verbose_name="备件编号")
    sp_type=models.ForeignKey(sp_type,verbose_name="备件类型")
    sp_company=models.ForeignKey(sp_company,verbose_name="备件厂商")
    amount=models.IntegerField(verbose_name="数量")
    status=models.CharField(max_length=1,verbose_name="当前状态")
    #taken_user=models.ForeignKey(my_user,verbose_name="领用人")
    #out_date=models.DateField(default=datetime.datetime.now,verbose_name="出库日期")
    #in_date=models.DateField(default=datetime.datetime.now,verbose_name="出库日期")
    warehouse_position=models.ForeignKey(warehouse_position,verbose_name="仓库地点")

    def __unicode__(self):
        return self.sp_id

admin.site.register(warehouse)
