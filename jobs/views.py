from django.shortcuts import render,redirect
from .models import Job
from django.core import serializers
import json
from django.db.models import Q
from django.shortcuts import HttpResponse

# autodelete
from django.core.management.base import BaseCommand, CommandError

from datetime import datetime, timedelta

from django.core.paginator import Paginator



# Create your views here.
def index(request):
    obj = (
        Job.objects.values(
            "position",
            "experience",
            "location",
            "company",
            "skills",
            "contact",
            "postdate",
        )
        .order_by("-postdate")
        .distinct()
    )
        
    locdata=Job.objects.values("location").distinct()
    loc=list(locdata)
    # loc=Job.objects.values('location').distinct()
    # domain=Job.objects.values('domain').distinct()

    job_data = list(obj)
    length = [i for i in range(1, len(job_data) + 1)]
    job_data = {"data": job_data, "len": length, "locdata":locdata}

    return render(request, "index.html", job_data)


def customfilter(request):

    filters = request.POST["searchkey"].split(" ")
    
    
    for filters in filters:
    
        filtered = (
            Job.objects.filter(
                Q(skills__contains=filters)
                | Q(location__contains=filters)
                | Q(position__contains=filters)
            )
            .order_by("-postdate")
            .distinct()
        )
    # loc=Job.objects.values('location').distinct()
    locdata=Job.objects.values("location").distinct()
    loc=list(locdata)
    job_data = list(filtered)
    job_data = {
        "data": job_data,
        "locdata":locdata
    }
    return render(request, "index.html", job_data)


def contact(request):
    return render(request, "contact.html")


def postjob(request):

    
    return render(request, "postjob.html")



def autdelete(request):
    Job.objects.filter(postdate__lte=datetime.now() - timedelta(days=30)).delete()

    return HttpResponse("Success")
