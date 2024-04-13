from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import *

import random
import string
 
def random_string(length):
    letters = string.ascii_letters + string.digits
    result = ''.join(random.choice(letters) for _ in range(length))
    return result

@csrf_exempt
def newnote(request):
    tmp=random_string(5)
    while NoteCon.objects.filter(id=tmp):
        tmp=random_string(5)
    return redirect('/'+tmp.lower())

@csrf_exempt
def download(request,ids):
    ids=ids.lower()
    try:
        obj=NoteCon.objects.all().get(id=ids)
        response = HttpResponse(obj.content, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}.txt"'.format(obj.id)
        return response
    except ObjectDoesNotExist:
        return HttpResponse("404",status=404)

@csrf_exempt
def writenote(request,ids):
    ids=ids.lower()
    if request.method=="GET":
        try:
            obj=NoteCon.objects.get(id=ids)
            res=render(request,"content.html",{"obj":obj})
            res["Cache-Control"]="no-cache"
            res["Pragma"]="no-cache"
            res["Expires"]="-1"
            return res
        except ObjectDoesNotExist:
            obj=NoteCon.objects.create(id=ids,content="")
            obj.save()
            res=render(request,"content.html",{"obj":obj})
            res["Cache-Control"]="no-cache"
            res["Pragma"]="no-cache"
            res["Expires"]="-1"
            return res
    else:
        print(request.POST.get("content"))
        obj=NoteCon.objects.get(id=ids)
        obj.content=request.POST.get("content")
        obj.save()
        res=HttpResponse()
        res["Cache-Control"]="no-cache"
        res["Pragma"]="no-cache"
        res["Expires"]="-1"
        return res