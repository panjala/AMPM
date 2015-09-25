from django.db import models
from django.core.validators import RegexValidator
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
# Create your models here.
# fresher details information
#from phonenumber_field.modelfields import PhoneNumberField
import pdb
class Profile (models.Model):
        #pdb.set_trace()
	name = models.CharField(max_length=30)
        surname = models.CharField(max_length=30)
        email = models.EmailField()
        phone_number = models.TextField(max_length=10,unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
        #phone_number = PhoneNumberField()
        ssc=models.IntegerField()
        inter=models.IntegerField()
        highest_qualification=models.CharField(max_length=10)
        #docfile = models.FileField(upload_to='documents/%Y/%m/%d')
        docfile = models.FileField(upload_to='')
        ppic = models.FileField(upload_to="ppic/")

class Careers(models.Model):
    firstname=models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()

class Exp(models.Model):
    primary=models.CharField(max_length=30)
    secondary=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    exp=models.IntegerField()
    ctc=models.FloatField(blank=True, null=True)
    exp_ctc=models.FloatField(blank=True, null=True)
    reason_for_change=models.TextField(max_length=1000)
    current_company=models.CharField(max_length=100)
    email = models.EmailField()
    docfile = models.FileField(upload_to='')

class Python(models.Model):
    Python=models.FloatField(blank=True, null=True)
    Django=models.FloatField(blank=True, null=True)
    Html=models.FloatField(blank=True, null=True)
    Linux=models.FloatField(blank=True, null=True)
    docfile = models.FileField(upload_to='')
    email = models.EmailField()



'''from django.contrib.gis.db import models


class Waypoint(models.Model):

    name = models.CharField(max_length=32)
    geometry = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)'''
    
