from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader


def index(request):
    context = {'Message':'Hello World'}
    return JsonResponse(context, safe=False)

def optionalHW(request):
    template = loader.get_template('HelloWorldMod/index.html')
    context = {
        'Message':'Hello World',
    }
    return HttpResponse(template.render(context, request))

#def index(request):
#    resp = {'Message':'Hello World'}
#    return JsonResponse(resp, safe=False) #HttpResponse(couldhavedonesomereallogic)