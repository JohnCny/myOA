# -*- coding: utf8 -*-
from django import forms
from models import *
from system_avalibe.models import *
import itertools



class accountForm(forms.ModelForm):
    def anyTrue(predicate, sequence):  
        return True in itertools.imap(predicate, sequence)  
    def endsWith(s, *endings):  
        return anyTrue(s.endswith, endings)
    
    class Meta:
        model=account
        exclude = ('user_id','approver',"modify_date","status","level","is_paid","pay_date","company")
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(accountForm, self).__init__(*args, **kwargs)
    
    def clean_amount(self):  
        amount = self.cleaned_data['amount']  
        if amount<=0:  
            raise forms.ValidationError("金额必须大于零")  
        return amount

    def clean_end_date(self):
        my_beg_date=self.cleaned_data['beg_date']
        my_end_date=self.cleaned_data['end_date']
        if my_beg_date>my_end_date:
            raise forms.ValidationError("开始日期必须小于结束日期")
        return my_end_date
    
