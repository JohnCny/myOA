"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from forms import *

class Account_manage_test (TestCase):
    def setUp(self):  
        self.account = {
            'beg_date':'2013-01-01',
            'modify_date':'2013-01-02',
            'end_date':'2013-01-03',
            'status':0,
            'approver':2,
            'level':1,
            'is_paid':0,
            'amount':1 
        }

        f = accountForm(self.account)  
        f.save()
        
    
    def test_price_positive(self):  
        f = accountForm(self.account)  
        self.assertFalse(f.is_valid())  
          
        self.accountForm['amount'] = 0  
        f = accountForm(self.account)  
        self.assertFalse(f.is_valid())  
          
        self.accountForm['amount'] = -1  
        f = accountForm(self.account)  
        self.assertFalse(f.is_valid())  
          
        self.accountForm['amount'] = 1



    


