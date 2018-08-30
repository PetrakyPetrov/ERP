from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import App

@login_required(login_url='/auth/login/')
def index(request):
    apps = App.objects.all()

    # for app in apps:
    #     classModel = app.model_class
    #     appDataCount = classModel.objects.all().count
    #     print(appDataCount)

    return render(request, 'apps-index.html', {'apps': apps})
