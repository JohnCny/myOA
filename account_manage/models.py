from django.db import models
import datetime
from django.contrib import admin
from system_avalibe.models import my_user
from system_avalibe.models import department
from system_avalibe.models import my_account_type
# Create your models here.

class account (models.Model):
    user_id=models.ForeignKey(my_user,related_name='user_id')
    department=models.ForeignKey(department)
    type_id=models.ForeignKey(my_account_type)
    amount=models.IntegerField()
    beg_date=models.DateField(default=datetime.datetime.now)
    modify_date=models.DateField(default=datetime.datetime.now)
    end_date=models.DateField(default=datetime.datetime.now)
    status=models.IntegerField(default=0)
    approver=models.ForeignKey(my_user,related_name="approver")
    
    def __unicode__(self):
        return self.amount

    class Meta:
        ordering = ['beg_date']

class account_show(admin.ModelAdmin):
    list_display=('user_id','department','beg_date')

admin.site.register(account)
