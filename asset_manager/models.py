from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    divice_serial = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField()
    checkout_condition = models.CharField(max_length=100)
    return_condition = models.CharField(max_length=100)

    def __str__(self):
        return self.name
