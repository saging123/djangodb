from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello")

def createView(request):
    context = {
        'title':'Create Product'
    }
    return render(request, 'productapp/create.html', context)


def viewer(request):
    context = {
        'title': 'View Products',
        'list':[
            {'name':'Lugod', 'price':90},
            {'name':'Habon', 'price':70},
            {'name':'ToothPaste', 'price':10}
        ]
    }
    return render(request, 'productapp/view.html',context)