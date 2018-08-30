from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect

from .forms import VehicleForm
from .models import Vehicle

@login_required(login_url='/auth/login/')
def index(requset):
    vehicles_list= Vehicle.objects.all()
    page = requset.GET.get('page', 1)
    paginator = Paginator(vehicles_list, 10)

    try:
        vehicles = paginator.page(page)
    except PageNotAnInteger:
        vehicles = paginator.page(1)
    except EmptyPage:
        vehicles = paginator.page(paginator.num_pages)

    return render(requset, 'fms-index.html', {'vehicles': vehicles})

@login_required(login_url='/auth/login/')
@permission_required('fms.add', raise_exception=True)
def createVehicle(request):
    form = VehicleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(index)

    return render(request, 'add-form.html', {'form': form, 'formName': 'Добавяне на МПС'})

@login_required(login_url='/auth/login/')
@permission_required('fms.edit', raise_exception=True)
def updateVehicle(request, id):
    contact = Vehicle.objects.get(id=id)
    form = VehicleForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        return redirect(index)

    return render(request, 'add-form.html', {'form': form, 'formName': 'Редактиране на МПС'})

@login_required(login_url='/auth/login/')
@permission_required('fms.delete', raise_exception=True)
def deleteVehicle(request, id):
    contact = Vehicle.objects.get(id=id)

    if request.method == 'GET':
        contact.delete()
        return redirect(index)

    # return render(request, 'list-contacts.html', {'form': 1})
