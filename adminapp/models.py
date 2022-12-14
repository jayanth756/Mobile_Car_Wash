from django.db import models
from django.conf import settings

# Database creation for teacher appintment.
class Appointment(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True,on_delete=models.DO_NOTHING)
	date=models.CharField(max_length=50)
	time_start=models.CharField(max_length=50)
	time_end=models.CharField(max_length=50)
	vechilenum=models.CharField(max_length=50)
	appointment_with=models.CharField(max_length=50,blank=True)
	update_time=models.DateField(auto_now=True, auto_now_add=False)
	frist_time=models.DateField(auto_now=False, auto_now_add=True)
	place = models.CharField(max_length=61)
    
    #show filed in adminapp panel
	def __str__(self):
		return self.date
	def __str__(self): 
		return self.time_start
	def __str__(self): 
		return self.time_end
	def __str__(self): 
		return self.vechilenum
	def __str__(self): 
		return self.appointment_with
	def __str__(self):
		return self.place