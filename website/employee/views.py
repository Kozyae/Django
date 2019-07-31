from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee, Sick, Annual, Unpay


class IndexView(generic.ListView):
    template_name = 'employee/index.html'
    context_object_name = 'all_employee'

    def get_queryset(self):
        return Employee.objects.all()


class DetailView(generic.DetailView):
    model = Employee
    template_name = 'employee/detail.html'


class Index2View(generic.ListView):
    template_name = 'employee/index2.html'
    context_object_name = 'all_sick'

    def get_queryset(self):
        return Sick.objects.all()

class DetailsickView(generic.DetailView):
    model = Sick
    template_name = 'employee/detail_sick.html'


class Index3View(generic.ListView):
    template_name = 'employee/index3.html'
    context_object_name = 'all_annual'

    def get_queryset(self):
        return Annual.objects.all()

class DetailannualView(generic.DetailView):
    model = Annual
    template_name = 'employee/detail_annual.html'


class Index4View(generic.ListView):
    template_name = 'employee/index4.html'
    context_object_name = 'all_unpay'

    def get_queryset(self):
        return Unpay.objects.all()

class DetailunpayView(generic.DetailView):
    model = Unpay
    template_name = 'employee/detail_unpay.html'



class Employeecreate(CreateView):
    model = Employee
    fields = ['firstName', 'lastName', 'nickName', 'phoneNumber', 'position',
              'create_at', 'update_at', 'leave', 'type', 'reason', 'startDate',
              'startTime', 'endDate', 'endTime', 'create_at1', 'update_at2']

class Employeeupdate(UpdateView):
    model = Employee
    fields = ['firstName', 'lastName', 'nickName', 'phoneNumber', 'position',
              'create_at', 'update_at', 'leave', 'type', 'reason', 'startDate',
              'startTime', 'endDate', 'endTime', 'create_at1', 'update_at2']

class Sickcreatesick(CreateView):
    model = Sick
    fields = ['employee', 'reason', 'startDate', 'startTime', 'endDate', 'endTime']

class Annualcreatesick(CreateView):
    model = Annual
    fields = ['employee', 'reason', 'startDate', 'startTime', 'endDate', 'endTime']

class Unpaycreatesick(CreateView):
    model = Unpay
    fields = ['employee', 'reason', 'startDate', 'startTime', 'endDate', 'endTime']

class Sickupdatesick(UpdateView):
    model = Sick
    fields = ['employee', 'reason', 'startDate', 'startTime', 'endDate', 'endTime']

class Annualupdateannual(UpdateView):
    model = Annual
    fields = ['employee', 'reason', 'startDate', 'startTime', 'endDate', 'endTime']

class Unpayupdateunpay(UpdateView):
    model = Unpay
    fields = ['employee', 'reason', 'startDate', 'startTime', 'endDate', 'endTime']



class Employeedelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee:index')

class Sickdelete(DeleteView):
    model = Sick
    success_url = reverse_lazy('employee:index2')

class Annualdelete(DeleteView):
    model = Annual
    success_url = reverse_lazy('employee:index3')

class Unpaydelete(DeleteView):
    model = Unpay
    success_url = reverse_lazy('employee:index4')