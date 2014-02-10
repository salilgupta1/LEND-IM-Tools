from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
#from django.contrib.auth.forms import UserCreationForm
from forms import LoginForm, RegistrationForm
from django.core.urlresolvers import reverse

def home_login(request):
	error = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			userName = request.POST.get('username','')
			passWord = request.POST.get('password','')
			user = auth.authenticate(username=userName, password = passWord)
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					return HttpResponseRedirect(reverse("clients:index"))
				else:
					error = "This account is no longer active!"
			else:
				error = "The login credentials are not correct!"
	else:
		form = LoginForm()
	context = {}
	context.update(csrf(request))
	context['login_form'] = form
	context['error'] = error
	return render(request,'tools/index.html',context)
		
def logOut(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse("home_login"))

def register_user(request):
	if request.method=='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST.get('username','')
			return HttpResponseRedirect(reverse('register_user_success',args=[username]))
	else:
		form = RegistrationForm()
	context = {}
	context.update(csrf(request))
	context['reg_form'] = form
	return render(request,'tools/register_user.html',context)

def register_user_success(request,username):
	return render(request,'tools/register_user_success.html',{"username":username})

