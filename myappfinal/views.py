from django.http import HttpResponse
from django.shortcuts import render 
from .models import Property
from .models import Area
from .models import Category
# Create your views here.
def about(request):
    # return HttpResponse('about')
    return render(request,template_name='about.html')
def contact(request):
    # return HttpResponse('about')
    return render(request,template_name='contact.html')
def error(request):
    # return HttpResponse('about')
    return render(request,template_name='error.html')
def index(request):
    # return HttpResponse('about')
    if request.method == "POST": 
        print(request.POST)
        searchCategory =request.POST.get('category')
        searchArea=request.POST.get('area')
        print(searchCategory)
        print(searchArea)
        propertysearch=Property.objects.filter(Category=searchCategory, Area=searchArea)
        return render(request,'index.html',{"data":propertysearch})
    else:
        displayproperty=Property.objects.all()
        print(displayproperty)
        return render(request,'index.html',{"data":displayproperty})

def propertyagent(request):
    # return HttpResponse('about')
    return render(request,template_name='propertyagent.html')

def propertylist(request):
    # return HttpResponse('about')
    return render(request,template_name='propertylist.html')

def propertytype(request):
    # return HttpResponse('about')
    return render(request,template_name='propertytype.html')

def testimonial(request):
    # return HttpResponse('about')
    return render(request,template_name='testimonial.html')