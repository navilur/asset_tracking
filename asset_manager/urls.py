from django.urls import path
from . import views

urlpatterns = [
    path("add_company/", views.add_company, name="add_company"),
    path("add_employees/", views.add_employees, name="add_employees"),
    path("add_devices/", views.add_devices, name="add_devices"),
    path("add_deviceslogs/", views.add_deviceslogs, name="add_deviceslogs"),
]
