# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from timeit import default_timer as timer
import statistics


from . import load

# Create your views here.from django.shortcuts import get_object_or_404, render

from .models import LimitesCommunes,Prefectures

def chargement(request):
    loadingTime = load.run()
    return render(request, 'limitesCommunes/load.html', {'loadingTime' : loadingTime})
    

def getLimite(request, gid):
    time = []
    for n in range(1000):
        start = timer()  
        feature = get_object_or_404(LimitesCommunes, id_geofla=gid)
        end = timer()
        time.append(start-end)
    statistics.mean(time)   
    return render(request, 'limitesCommunes/base.html', {'feature': feature, 'time' : time})

def getLimites(request, id_geofla):
    print(timeit.timeit('map(get_object_or_404(limitesCommunes, gid__in=gid_value),gid_value)'))
    features = LimitesCommunes.objects.all()
    return render(request, 'limitesCommunes/get.html', {'features': features, 'time' : time})

def getPrefecture(request, gid):
    print(timeit.timeit('map(get_object_or_404(limitesCommunes, gid__in=gid_value),gid_value)'))
    feature = get_object_or_404(Prefectures, id_geofla=id_geofla)
    return render(request, 'limitesCommunes/get.html', {'features': feature, 'time' : time})
    
def getPrefectures(request, gid):
    print(timeit.timeit('map(get_object_or_404(limitesCommunes, gid__in=gid_value),gid_value)'))
    features = LimitesCommunes.objects.all()
    return render(request, 'limitesCommunes/get.html', {'features': features, 'time' : time})
    
    
#~ def timeit_getfeatures(request,gid_list):
    #~ print(timeit.timeit('map(get_list_or_404(limitesCommunes, gid__in=gid_list), gid_list)'))
