# -*- coding: utf-8 -*-
from TestModel.models import Document,DataDB
from django.shortcuts import render_to_response,render
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponse, Http404, FileResponse
import csv,time,os,random,math
import numpy as np
import pandas as pd
from sklearn.externals import joblib
# 数据库操作

def saveData(request):
    return render_to_response('data/upload.html')
def downloadData(request):
    document = Document.objects.filter()
    print(type(document))
    return render(request,'data/download.html',{'list': document})


def loadDB(fileDIR):
    file = pd.read_csv(open(fileDIR))
    # clf=joblib.load("static/trainModel/clf.pkl")
    # label_list=[]
    # to_list = clf.predict(file)
    # for i in to_list:
    #     label_list.append(i)     
    # file["label"] = label_list
    # file.to_csv(fileDIR,encoding='utf-8')
    # print("over")
    # file = pd.read_csv(open(fileDIR))
    # for index, row in file.iterrows():
    #     print(index)
    #     data = DataDB(
    #         id=int(math.ceil(time.time())%10000000 + index),
    #         count = row['count'],
    #         srv_count  = row['srv_count'],
    #         dst_host_count = row['dst_host_count'],
    #         dst_host_srv_count = row['dst_host_srv_count'],
    #         same_srv_rate = row['same_srv_rate'],
    #         dst_host_same_src_port_rate = row['dst_host_same_src_port_rate'],
    #         dst_host_serror_rate = row['dst_host_serror_rate'],
    #         label = row['label']           
    #     )
    #     data.save()






def saveDB(request):
    context = {}
    print("save ====================")
    if(request.method=="POST"):
        fileID = str(math.ceil(time.time())%10000000)+"_" +str(int(random.random()*10))
        while(Document.objects.filter(id=fileID).exists()):
            fileID = str(math.ceil(time.time()))+"_" +str(int(random.random()*10))
        fileObject = request.FILES.get('cvsFile')
        print("save ====================" + str(fileObject))
        if(fileObject!=None):
            fileDIR = "static/dataSave/" + fileID + "_" + fileObject.name
            print(fileDIR)
            file = open(fileDIR,'wb')
            for item in fileObject.chunks():
                file.write(item)
            file.close()
            loadDB(fileDIR)
            document = Document(
                id = fileID,
                dir = fileDIR,
                name = fileObject.name
            )
            document.save()
            context['code'] = 1
            context['text'] = "成功上传"
        else:
            context['code'] = -2
            context['text'] = "空文件"
            return render_to_response('data/upload.html')
    else:
        context['code'] = -3
        context['text'] = "协议错误"
    return JsonResponse(context)

    
def downloadDB(request):
    context = {}
    print("start=====================")
    if(request.method == "POST"):
        fileID = request.POST.get('fileID', '')
        if(fileID != ''):
            print("start=====================" + str(fileID))
            fileList = Document.objects.filter(id = fileID)
            if(not fileList.exists()):
                context['code'] = -2
                context['text'] = "文件为空"
            else:
                print(fileList[0].dir)
                print("open file")
                print("name " + str(fileList[0].dir.split('/')[-1]))
                # response = FileResponse(f)
                # response['Content-Type'] = 'application/octet-stream'
                # response['Content-Disposition'] = 'attachment;filename="'+fileList[0].dir.split('/')[-1] + '"'

                context['dir'] = '/' + fileList[0].dir

                # response = HttpResponse(f,content_type='application/vnd.ms-excel')
                # response['Content-Disposition'] = "attachment"
                return JsonResponse(context)
    else:
        context['code'] = -3
        context['text'] = "协议错误"
    return JsonResponse(context) 

