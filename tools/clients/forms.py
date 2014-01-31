from models import Client
from django import forms
import uuid

class ClientForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
    	super(ClientForm,self).__init__(*args,**kwargs)
    	self.fields['b_name'].label = "Business Name"
    	for fields in self.fields.items():
			fields[1].widget.attrs.update({'class':'form-control'})       
    class Meta:
        model = Client
        exclude = ['client_uuid']