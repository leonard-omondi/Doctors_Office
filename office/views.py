from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PatientSignUpForm, DoctorSignUpForm, EmployeeSignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def home(request):
    return render(request, 'office/home.html')


def about(request):
    return render(request, 'office/about.html')


def register(request):
    return render(request, 'office/register.html')


def patient(request):
    return render(request, 'office/patient.html')


@login_required
def patient_profile(request):
    return render(request, 'office/patient_profile.html')


def employee(request):
    return render(request, 'office/employee.html')


def doctor(request):
    return render(request, 'office/doctor.html')


def patient_register(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, you can now log in.')
            return redirect('office-home')
    else:
        form = PatientSignUpForm()
    return render(request, 'office/patient_registration.html', {'form': form})


def employee_register(request):
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, you can now log in.')
            return redirect('office-home')
    else:
        form = EmployeeSignUpForm()
    return render(request, 'office/employee_registration.html', {'form': form})


def doctor_register(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, you can now log in.')
            return redirect('office-home')
    else:
        form = DoctorSignUpForm()
    return render(request, 'office/employee_registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('office-home')


def login_request(request):
    form = AuthenticationForm(data=request.POST or None)
    msg = None
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_patient:
            login(request, user)
            return redirect('office-patient')
        elif user is not None and user.is_doctor:
            login(request, user)
            return redirect('office-doctor')
        elif user is not None and user.is_employee:
            login(request, user)
            return redirect('office-employee')
        else:
            msg = 'error validating form'

    return render(request, 'office/test_login.html', {'form': form, 'msg': msg})
