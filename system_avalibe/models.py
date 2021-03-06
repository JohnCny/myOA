from django.db import models
import datetime
from django.contrib import admin

# Create your models here.

class department(models.Model):
    department_name=models.CharField(max_length=16)
    parent_id=models.IntegerField()

    def __unicode__(self):
        return self.department_name
    
class position(models.Model):
    department=models.ForeignKey(department)
    position_name=models.CharField(max_length=64)
    position_grade=models.IntegerField()

    def __unicode__(self):
        return self.position_name

class my_user(models.Model):
    login_name=models.CharField(max_length=16)
    login_password=models.CharField(max_length=16)
    real_name=models.CharField(max_length=16)
    telephone=models.CharField(max_length=16)
    mobilephone=models.CharField(max_length=16)
    position=models.ForeignKey(position)
    department=models.ForeignKey(department)
    last_login_date=models.DateTimeField(default=datetime.datetime.now)
    birthday=models.DateTimeField(default=datetime.datetime.now)
    company=models.IntegerField()

    def __unicode__(self):
        return self.login_name

class my_account_type(models.Model):
    department=models.ForeignKey(department)
    type_name=models.CharField(max_length=20)

    def __unicode__(self):
        return self.type_name

class sp_company(models.Model):
    sp_company_name=models.CharField(max_length=16)

    def __unicode__(self):
        return self.sp_company_name

class sp_type(models.Model):
    sp_company=models.ForeignKey(sp_company)
    sp_type_name=models.CharField(max_length=20)

    def __unicode__(self):
        return self.sp_type_name

class warehouse_position(models.Model):
    position_name=models.CharField(max_length=16)
    parent=models.IntegerField()
    
    def __unicode__(self):
        return self.position_name

admin.site.register(my_user)
admin.site.register(my_account_type)
admin.site.register(department)
admin.site.register(position)
