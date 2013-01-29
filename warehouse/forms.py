
from django import forms
from models import *



class warehouseForm(forms.ModelForm):
	
    class Meta:
        model = warehouse	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(warehouseForm, self).__init__(*args, **kwargs)

