
from django.urls import path
from.views import register_patient
from.views import patient_list

urlpatterns = [
    path("register/",register_patient,name="register_patient"),
    path('list/',patient_list,name="patient_list"),
]
