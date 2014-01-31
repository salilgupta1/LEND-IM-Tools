from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,HttpResponse
from models import Client
from forms import ClientForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core import serializers

def ajax_coordinates(request):
	if request.is_ajax():
		subset = request.GET['type']
		if subset not in ["all","BTP","LOAN"]:
			clients = Client.objects.get(client_uuid = subset)
			json_data = serializers.serialize("json",[clients],fields = ("latitude","longitude","first_name","last_name"))
		else:
			if subset == "all":
				clients = Client.objects.all()
			else:
				clients = Client.objects.filter(client_type = subset)
			json_data = serializers.serialize("json",clients,fields = ("latitude","longitude","first_name","last_name"))
	return HttpResponse(json_data,content_type = "application/json")

@login_required
def index (request):
	clients = Client.objects.all()
	context = {"clients":clients}
	return render(request,"clients/index.html",context)

@login_required
def client(request,clientType):
	clients = Client.objects.filter(client_type = clientType)
	context = {"clients":clients,"clientType":clientType}
	return render(request,"clients/clients.html",context)

@login_required
def create_client(request):
	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("clients:index"))
	else:
		form = ClientForm()
	context = {}
	context.update(csrf(request))
	context['create_form'] = form
	return render(request,"clients/createClient.html",context)

@csrf_exempt #need to fix this how to add a csrf_token to the form
def delete_client(request):
	uuid = request.POST['uuid']
	c = Client.objects.get(client_uuid = uuid)
	x = c.client_type
	c.delete()
	#return HttpResponseRedirect(reverse(request.META['HTTP_REFERER']))
	if x == "LOAN":
		return HttpResponseRedirect(reverse("clients:loan"))
	else:
		return HttpResponseRedirect(reverse("clients:btp"))

@login_required
def edit_client(request,client_UUID):
	c = Client.objects.get(client_uuid = client_UUID)
	if request.method == 'POST':
		form = ClientForm(request.POST,instance = c)
		if form.is_valid():
			client_UUID = c.client_uuid
			form.save()
			return HttpResponseRedirect(reverse("clients:edit_client",args =[client_UUID]))
	else:
		form = ClientForm(instance = c)
	context = {}
	context.update(csrf(request))
	context['model_form'] = form
	context['title'] = c
	context['uuid'] = client_UUID
	return render(request,"clients/editClient.html",context)
