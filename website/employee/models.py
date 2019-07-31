from django.db import models
from django.urls import reverse



class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nickName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10)
    position = models.CharField(max_length=100)
    create_at = models.CharField(max_length=100)
    update_at = models.CharField(max_length=100)
    leave = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)
    startTime = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    endTime = models.CharField(max_length=100)
    create_at1 = models.CharField(max_length=100)
    update_at2 = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('employee:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.firstName + '-' + self.lastName

class Sick(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)
    startTime = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    endTime = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('employee:detail_sick', kwargs={'pk': self.pk})

    def __str__(self):
        return self.reason

class Annual(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)
    startTime = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    endTime = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('employee:detail_annual', kwargs={'pk': self.pk})

    def __str__(self):
        return self.reason

class Unpay(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)
    startTime = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    endTime = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('employee:detail_unpay', kwargs={'pk': self.pk})

    def __str__(self):
        return self.reason