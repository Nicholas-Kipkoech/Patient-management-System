from statistics import mode
from django.db import models
from django.forms import DateField, NumberInput, TextInput
from django.urls import clear_script_prefix

class Patient(models.Model):
    patient_number=models.CharField(max_length=15,null=True,unique=True)
    registration_date=models.DateField()
    first_name=models.CharField(max_length=17,null=True)
    last_name=models.CharField(max_length=20,null=True)
    date_of_birth=models.DateTimeField()
    gender_choice=(
        ("male","Male"),
        ("female","Female"),
        ("other","Other"),
    )
    gender=models.CharField(max_length=17,choices=gender_choice,null=True)
    
    
# class Vitals(models.Model):
#         patient_name=models.ForeignKey(max_length=15,null=True,unique=True)
#         visit_date=DateField()
#         height=TextInput()
#         weight=TextInput()
#         BMI=NumberInput()
    
