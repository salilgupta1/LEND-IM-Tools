from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255,error_messages={'required':'Please input a username'}, widget = forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control"}),error_messages = {'required':'Please Input a password'})

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(error_messages = {"invalid":"The email given is not valid!", "required":"Please input an email"})
	first_name = forms.CharField(max_length = 50, error_messages = {'required':"You must have a first name right?","max_length":"There is no way that your first name is that long...."})
	last_name = forms.CharField(max_length = 50, error_messages = {'required':"You must have a last name right?","max_length":"There is no way that your last name is that long...."})

	class Meta:
		model = User
		fields = ("username","first_name","last_name","email","password1","password2")
	def save(self,commit=True):
		user = super(RegistrationForm,self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user
	def __init__(self, *args, **kwargs):
		super(RegistrationForm,self).__init__(*args,**kwargs)
		for fields in self.fields.items():
			fields[1].widget.attrs.update({'class':'form-control'}) 