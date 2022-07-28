from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Patient


class PatientRegistrationForms(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        # fields = ['patient_number', 'registration_date', 'first_name', 'last_name', 'date_of_birth','gender']
        widgets = {
            'patient_number': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:99%'}),
            'regstration_date': forms.DateTimeInput(attrs={'class': 'form-control', 'style': 'width:88%'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:99%', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:99%', }),
            'date_of_birth': forms.DateField(widget=AdminDateWidget(), attrs={'class': 'form-control', 'style': 'width:99%', }),
            'gender': forms.Select(attrs={'class': 'form-select', 'style': 'width:99%'}),
        }
