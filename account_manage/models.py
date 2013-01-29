# -*- coding: utf8 -*-
from django.db import models
import datetime
from django.contrib import admin
from system_avalibe.models import my_user
from system_avalibe.models import department
from system_avalibe.models import my_account_type
# Create your models here.

class account (models.Model):
    user_id=models.ForeignKey(my_user,related_name='user_id',verbose_name="用户")
    department=models.ForeignKey(department,verbose_name="所属部门")
    type_id=models.ForeignKey(my_account_type,verbose_name="费用类型")
    amount=models.IntegerField(verbose_name="金额")
    beg_date=models.DateField(default=datetime.datetime.now,verbose_name="费用开始日期")
    modify_date=models.DateField(default=datetime.datetime.now,verbose_name="修改日期")
    end_date=models.DateField(default=datetime.datetime.now,verbose_name="费用结束日期")
    status=models.IntegerField(default=0,verbose_name="当前状态")
    approver=models.ForeignKey(my_user,related_name="approver",verbose_name="审核人")
    level=models.IntegerField(default=0,verbose_name="级别") 
    is_paid=models.IntegerField(default=0,verbose_name="是否付款")
    pay_date=models.DateField(default=None,verbose_name="付款日期")
    company=models.IntegerField(default=0,verbose_name="公司")
    def __unicode__(self):
        return str(self.amount)

    class Meta:
        ordering = ['beg_date']

class account_show(admin.ModelAdmin):
    list_display=('user_id','department','beg_date')

admin.site.register(account)

