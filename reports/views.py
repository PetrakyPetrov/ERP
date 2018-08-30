import json
import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count, QuerySet
from django.utils.safestring import mark_safe

from companies.models import Company
from fms.models import Vehicle
from hrs.models import Employee, JobPosition


@login_required(login_url='/auth/login/')
def index(requset):
    salaries = Employee.objects.values('salary')
    numberOfEmployees = Employee.objects.all().count()
    jobPositions = JobPosition.objects.all()
    companies = Company.objects.all()

    numberOfSalaries = 0
    sumOfSalaries = 0

    companyEmployees = list()
    companyVehicles = list()

    jobNames = list()
    jobEmployees = list()
    employeePerJobPosition = {}
    jobColors = list()

    for jobPosition in jobPositions:
        jobNames.append(jobPosition.name)
        jobEmployees.append(Employee.objects.filter(job_position=jobPosition.id).count())
        r = lambda: random.randint(0, 255)
        jobColors.append('#%02X%02X%02X' % (r(), r(), r()))

    employeePerJobPosition['positions'] = jobNames
    employeePerJobPosition['employees'] = jobEmployees
    employeePerJobPosition['colors'] = jobColors

    employeePerCompany = {}
    vehiclePerCompany = {}
    companyColors = []
    companyNames = list()

    for company in companies:
        r = lambda: random.randint(0, 255)
        companyColors.append('#%02X%02X%02X' % (r(), r(), r()))

        companyNames.append(company.name)
        companyEmployees.append(Employee.objects.filter(company=company.id).count())
        companyVehicles.append(Vehicle.objects.filter(company_owner=company.id).count())

    employeePerCompany['employees'] = companyEmployees
    employeePerCompany['companies'] = companyNames
    employeePerCompany['colors'] = companyColors

    vehiclePerCompany['companies'] = companyNames
    vehiclePerCompany['vehicles'] = companyVehicles
    vehiclePerCompany['colors'] = companyColors

    for salary in salaries:
        sumOfSalaries += salary['salary']
        numberOfSalaries += 1

    averageSalary = sumOfSalaries / numberOfSalaries

    return render(requset, 'reports.html', {
        'employeePerJobPosition': mark_safe(json.dumps(employeePerJobPosition)),
        'numberOfEmployees': numberOfEmployees,
        'averageSalary': averageSalary,
        'sumOfSalaries': sumOfSalaries,
        'employeePerCompany': mark_safe(json.dumps(employeePerCompany)),
        'vehiclePerCompany': mark_safe(json.dumps(vehiclePerCompany)),

    })