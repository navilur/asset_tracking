from django.urls import path
from . import views

urlpatterns = [
    path("add_company/", views.add_company, name="add_company"),
    path("add_employees/", views.add_employees, name="add_employees"),
    path("add_devices/", views.add_devices, name="add_devices"),
    path("add_deviceslogs/", views.add_deviceslogs, name="add_deviceslogs"),
    path("company_list/", views.company_list, name="company_list"),
    path("employees_list/", views.employees_list, name="employees_list"),
    path("devices_list/", views.devices_list, name="devices_list"),
    path("deviceslogs_list/", views.deviceslogs_list, name="deviceslogs_list"),
]
