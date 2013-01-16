# -*- coding: utf8 -*-
from django import forms
from models import *
from system_avalibe.models import *



class accountForm(forms.ModelForm):
    class Meta:
        model=account
        exclude = ('user_id','approver',"modify_date","status","level",)
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(accountForm, self).__init__(*args, **kwargs)

