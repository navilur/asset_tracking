from django.shortcuts import render, redirect
from .forms import *
from .models import *


def add_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("company_list")
    else:
        form = CompanyForm()
    return render(request, "add_company.html", {"form": form})


def company_list(request):
    company = Company.objects.all()
    return render(request, "company_list.html", {"company": company})


def add_employees(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employees_list")
    else:
        form = EmployeeForm()
    return render(request, "add_employees.html", {"form": form})


def employees_list(request):
    employee = Employee.objects.all()
    return render(request, "employees_list.html", {"employee": employee})


def add_devices(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("devices_list")
    else:
        form = DeviceForm()
    return render(request, "add_devices.html", {"form": form})


def devices_list(request):
    device = Device.objects.all()
    return render(request, "devices_list.html", {"device": device})


def add_deviceslogs(request):
    if request.method == "POST":
        form = DeviceLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("deviceslogs_list")
    else:
        form = DeviceLogForm()
    return render(request, "add_deviceslogs.html", {"form": form})


def deviceslogs_list(request):
    device_logs = DeviceLog.objects.all()
    return render(request, "deviceslogs_list.html", {"device_logs": device_logs})
