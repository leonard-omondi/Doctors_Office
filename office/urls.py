from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='office-home'),
    path('about/', views.about, name='office-about'),
    path('patient/', views.patient, name='office-patient'),
    path('patient_profile/', views.patient_profile, name='office-patient_profile'),
    path('doctor/', views.doctor, name='office-doctor'),
    path('employee/', views.employee, name='office-employee'),

]
