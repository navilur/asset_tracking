from django import forms
from .models import Company, Employee, Device, DeviceLog


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("name",)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("company", "name", "emp_id")


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = (
            "name",
            "divice_serial",
            "condition",
        )


class DeviceLogForm(forms.ModelForm):
    class Meta:
        model = DeviceLog
        fields = (
            "device",
            "employee",
            "company",
            "name",
            "checkout_date",
            "return_date",
            "checkout_condition",
            "return_condition",
        )
