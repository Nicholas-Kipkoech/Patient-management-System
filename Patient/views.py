
from .models import Patient
from django import forms
from django.shortcuts import render
from.forms import PatientRegistrationForms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.views import generic
from .models import Patient

def register_patient(request):
    if request.method== "POST":
        form=PatientRegistrationForms(request.POST,request.FILES,)
        if form.is_valid():
         form.save()
        else:
            print(form.errors)
    else:
        form=PatientRegistrationForms()
    return render(request,"register_patient.html",{"form":form})

def patient_list(request):
    patients=Patient.objects.all()
    return render(request,"patient_list.html",{"patients":patients})  



class CreateView(generic.edit.CreateView):
    model = Patient
    fields = ['patient_text', 'pub_date']
    def get_form(self):
        form = super().get_form()
        form.fields['pub_date'].widget = DateTimePickerInput()
        return form