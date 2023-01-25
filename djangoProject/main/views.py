from django.shortcuts import render
from .models import *
from django.conf import settings
# Create your views here.


def index(request):
    data = DataMain.objects.all()
    print(settings.BASE_DIR)
    return render(request, "main/index.html", {"data": data})


def demand(request):
    data_demand = DataDemand.objects.all()
    return render(request, "main/demand.html", {"dataDemand": data_demand})


def geography(request):
    data_geo = DataGeo.objects.all()
    return render(request, "main/geography.html", {"dataGeo": data_geo})


def skills(request):
    data_skills = DataSkills.objects.all()
    return render(request, "main/skills.html", {"dataSkills": data_skills})


def recentvacancies(request):
    data_rec_vac = DataRecVac.objects.all()
    return render(request, "main/recentvacancies.html", {"dataRecVac": data_rec_vac})
