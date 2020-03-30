# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from TestModel.models import DataDB
import csv
import time
import os




def diagram(request):
    dataList = DataDB.objects.filter()
    return render(request,'data/diagram.html',{'dataList':dataList[:100]})



