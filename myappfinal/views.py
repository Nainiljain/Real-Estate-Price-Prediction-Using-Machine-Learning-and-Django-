from django.http import HttpResponse
from django.shortcuts import render 
from .models import Property
from .models import Area
from .models import Category
# Create your views here.
def property(request):
    propertyId = request.GET.get('property')
    print("p",propertyId)
    if propertyId:
        displayresult = Property.objects.filter(id=propertyId).values()
    print(displayresult)
    return render(request,'property.html',{'property':displayresult[1]})

    displayresult = Property.objects.all()
    return render(request,'property.html',{'data':displayresult})
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
    # return HttpResponse('index')
    
    if request.method == "POST":
        c =request.POST.get('category')
        a=request.POST.get('area')
        v=request.POST.get('feature')    
        print("Category ",c)
        print("Area ",a)
        print("Feature ",v)
        if c=="Category" and a=="Area" and v=="All Properties":
            displayresult=Property.objects.all()
            return render(request,'index.html',{"data":displayresult})
        elif c!="Category" and a=="Area" and v=="All Properties":
            displayresult = Property.objects.filter(Category = c).values()
            return render(request,'index.html',{"data":displayresult})
        elif c!="Category" and a!="Area" and v=="All Properties":
            displayresult = Property.objects.filter(Category = c,Area = a).values()
            return render(request,'index.html',{"data":displayresult})
        elif c=="Category" and a=="Area" and v!="All Properties":
            displayresult = Property.objects.filter(PropertySellorRent = v).values()
            return render(request,'index.html',{"data":displayresult})
        elif c!="Category" and a=="Area" and v!="All Properties":
            displayresult = Property.objects.filter(Category = c,PropertySellorRent = v).values()
            return render(request,'index.html',{"data":displayresult})
        elif c=="Category" and a!="Area" and v!="All Properties":
            displayresult = Property.objects.filter(Area = a,PropertySellorRent = v).values()
            return render(request,'index.html',{"data":displayresult})
        elif c=="Category" and a!="Area" and v=="All Properties":
            displayresult = Property.objects.filter(Area = a).values()
            return render(request,'index.html',{"data":displayresult})        
    else:
        displayresult=Property.objects.all()
        print(displayresult)
        return render(request,'index.html',{'data':displayresult})
        property=Property.objects.all()
        print(property)
        return render(request,'index.html',{'data':property})
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