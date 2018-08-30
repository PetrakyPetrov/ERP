from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.core import serializers
from django.http import JsonResponse

@login_required(login_url='/auth/login/')
def index(requset):
    return redirect(listContacts)

@login_required(login_url='/auth/login/')
def listContacts(requset):
    contacts_list = Contact.objects.all()
    page = requset.GET.get('page', 1)
    paginator = Paginator(contacts_list, 10)

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(requset, 'list-contacts.html', {'contacts': contacts})

@login_required(login_url='/auth/login/')
def searchContact(request):
    contacts = Contact.objects.filter(name__contains=request.POST['search'])
    return render(request, 'list-contacts.html', {'contacts': contacts})

@login_required(login_url='/auth/login/')
@permission_required('contacts.add', raise_exception=True)
def createContact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(listContacts)

    return render(request, 'add-form.html', {'form': form, 'formName': 'Добавяне на контакт'})

@login_required(login_url='/auth/login/')
@permission_required('contacts.edit', raise_exception=True)
def updateContact(request, id):
    contact = Contact.objects.get(id=id)
    form = ContactForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        return redirect(listContacts)

    return render(request, 'add-form.html', {'form': form, 'formName': 'Редактиране на контакт'})

@login_required(login_url='/auth/login/')
@permission_required('contacts.delete', raise_exception=True)
def deleteContact(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == 'GET':
        contact.delete()
        return redirect(listContacts)

    # return render(request, 'list-contacts.html', {'form': 1})
