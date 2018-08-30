from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import EmployeeForm
from .models import Employee
from .models import JobPosition


@login_required(login_url='/auth/login/')
def index(requset):
    employees_list = Employee.objects.all()
    page = requset.GET.get('page', 1)
    paginator = Paginator(employees_list, 10)

    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    return render(requset, 'hr-index.html', {'employees': employees})

@login_required(login_url='/auth/login/')
def searchEmployee(request):
    employees = Employee.objects.filter(Q(phone_number__contains=request.POST['search']) | Q(company__name__contains=request.POST['search']))
    return render(request, 'hr-index.html', {'employees': employees})

@login_required(login_url='/auth/login/')
@permission_required('hrs.add', raise_exception=True)
def createEmployee(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(index)

    return render(request, 'add-form.html', {'form': form, 'formName': 'Добавяне на служител'})

@login_required(login_url='/auth/login/')
@permission_required('hrs.edit', raise_exception=True)
def updateEmployee(request, id):
    contact = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        return redirect(index)

    return render(request, 'add-form.html', {'form': form, 'formName': 'Редактиране на служител'})

@login_required(login_url='/auth/login/')
@permission_required('hrs.delete', raise_exception=True)
def deleteEmployee(request, id):
    contact = Employee.objects.get(id=id)

    if request.method == 'GET':
        contact.delete()
        return redirect(index)

    # return render(request, 'list-contacts.html', {'form': 1})


