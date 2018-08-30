from django.contrib.auth.decorators import login_required, permission_required
from django.core.checks import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from .forms import CompanyForm
from .models import Company

@login_required(login_url='/auth/login/')
def index(requset):
    companies = Company.objects.all()
    return render(requset, 'list-companies.html', {'companies': companies})

@login_required(login_url='/auth/login/')
def listCompanies(requset):
    companies_list = Company.objects.all()
    page = requset.GET.get('page', 1)
    paginator = Paginator(companies_list, 1)

    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        companies = paginator.page(1)
    except EmptyPage:
        companies = paginator.page(paginator.num_pages)

    return render(requset, 'list-companies.html', {'companies': companies})

@login_required(login_url='/auth/login/')
@permission_required('companies.add', raise_exception=True)
def createCompany(request):
    form = CompanyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(index)

    return render(request, 'add-form.html', {'form': form, 'formName': 'Добавяне на фирма'})

@login_required(login_url='/auth/login/')
@permission_required('companies.edit', raise_exception=True)
def updateCompany(request, id):
    contact = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()

        return redirect(index)

    return render(request, 'add-form.html', {'form': form, 'formName': 'Редактиране на фирма'})

@login_required(login_url='/auth/login/')
@permission_required('companies.delete', raise_exception=True)
def deleteCompany(request, id):
    contact = Company.objects.get(id=id)

    if request.method == 'GET':
        contact.delete()
        return redirect(index)

    # return render(request, 'list-contacts.html', {'form': 1})
