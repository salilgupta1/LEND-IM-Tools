from django.db import models
import uuid

# Create your models here.
class Client(models.Model):
	client_uuid = models.CharField(max_length = 100, default = uuid.uuid4, primary_key = True)
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	CLIENT_TYPE = (("LOAN","Loan"),("BTP","Btp"))
	client_type = models.CharField(max_length=10, choices = CLIENT_TYPE)
	b_name = models.CharField(max_length = 100)
	loan_amount = models.PositiveIntegerField(null = True,blank = True)
	repayment_time = models.PositiveIntegerField(null = True, blank = True)
	email = models.EmailField(max_length=254)
	staff_member = models.CharField(max_length=255)
	latitude = models.FloatField("Latitude", null = True, blank = True)
	longitude = models.FloatField('Longitude',null =True, blank = True)
	
	def __unicode__(self):
		return self.first_name +" "+ self.last_name 
