from django.http import HttpResponse
import os
import pickle
import numpy as np
from django.shortcuts import render 
from .models import Property, Subcategory
from .models import Area
from .models import Category
from .forms import RatechangePredictionForm
from .models import Contactform
# Create your views here.
def rate_change(request):
    #return HttpResponse
    print(request)
    if request.method == 'POST':
        category = float(request.POST.get("opr"))

        residentialtype = request.POST.get("residential")
        if residentialtype == None or residentialtype =='':
            residentialtype=0
        else:
            residentialtype = float(residentialtype)
         
        commercialtype = (request.POST.get("commercial")) 
        if commercialtype == None or commercialtype =='':
            commercialtype=0
        else:
            commercialtype = float(commercialtype)    
        size = float(request.POST.get("size"))
        Luxury = float(request.POST.get("luxury"))
        location = float(request.POST.get("location"))
        subcategory = float(request.POST.get("category"))
        Age = float(request.POST.get("Age"))
        Ameneties = float(request.POST.get("Ameneties"))
        pice = float(request.POST.get("price"))
        choice = float(request.POST.get("choice"))
        print('catory',category)
        print('residential',residentialtype)
        print('commercial',commercialtype)
        print('size',size)
        print('luxury',Luxury)
        print('location',location)
        print('subcategory',subcategory)
        print('age',Age)
        print('ameneties',Ameneties)
        print('pice',pice)
        print('choice',choice)
        form = RatechangePredictionForm(request.POST)
      
        list=[category,residentialtype,commercialtype,size,Luxury,location,subcategory,Age,Ameneties,pice,choice]
        with open('classifierforsell.pkl','rb') as file:
            clf = pickle.load(file)   
            
            # Extract input data from the form
            new_data = np.array(list).reshape(1, -1)

            # Perform prediction
            rate_change = clf.predict(new_data)[0]

            # Prepare the response  
            context = {
                'form': form,
                'rate_change': round(rate_change, 2),
            }
            print('p')
            return render(request, 'prediction.html', context)
    else:
        form = RatechangePredictionForm()

    context = {'form': form}
    return render(request, 'prediction.html', context)

def singleproperty(request):
    propertyId = request.GET.get('property')
    print("p",propertyId)
    if propertyId:
        displayresult = Property.objects.filter(id=propertyId).order_by('?')
        
    print(displayresult)
    return render(request,'property.html',{'property':displayresult[0]})

def about(request):
    # return HttpResponse('about')
    return render(request,template_name='about.html')
def contact(request):
    # return HttpResponse('about')
    if request.method == 'GET':
        return render(request,template_name='contact.html')    
    if request.POST !=None:
        name=request.POST.get("Name")
        email = request.POST.get("Email")
        subject = request.POST.get("Subject")
        message = request.POST.get("Message")
        print(name)
        print(email)
        print(subject)
        print(message)
        contactobj = Contactform()
        contactobj.name = name
        contactobj.email = email
        contactobj.subject = subject
        contactobj.message= message
        contactobj.save()

    return render(request,template_name='contact.html')
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


def testimonial(request):
    # return HttpResponse('about')
    return render(request,template_name='testimonial.html')

def AddProperty(request):
    #return HttpResponse('jquery')

    if request.method == 'GET':
        return render(request,template_name='AddProperty.html')  
    if request.POST !=None:
        PropertyName=request.POST.get("Property Name")
        Areaid=request.POST.get("Area Name")
        Categoryid = request.POST.get("category")
        Subcategoryid = request.POST.get("subcategory")
        PropertyTitle = request.POST.get("Property title")
        PropertySellorRent = request.POST.get("propertyType")
        PropertyAmount = request.POST.get("price")
        PropertyFromDate = request.POST.get("availabilityStart")
        PropertyImage = request.FILES["file"]
        PropertyToDate = request.POST.get("availabilityEnd")
        PropertyStatus = request.POST.get("Property status")
        print(PropertyName)
        print(Areaid)
        print(Categoryid)
        print(Subcategoryid)
        print(PropertyTitle)
        print(PropertySellorRent)
        print(PropertyAmount)
        print(PropertyFromDate)
        print(PropertyImage)
        print(PropertyToDate)
        print(PropertyStatus)
        area_object = Area.objects.get(pk=Areaid)
        category_object = Category.objects.get(pk=Categoryid)
        Subcategory_object = Subcategory.objects.get(pk=Subcategoryid)    
        propertyobj = Property()
        propertyobj.PropertyName = PropertyName
        propertyobj.Area = area_object
        propertyobj.Category = category_object
        propertyobj.Subcategory = Subcategory_object
        propertyobj.PropertyTitle = PropertyTitle
        propertyobj.PropertySellorRent = PropertySellorRent
        propertyobj.PropertyAmount = PropertyAmount
        propertyobj.PropertyFromDate = PropertyFromDate
        propertyobj.PropertyImage = PropertyImage
        propertyobj.PropertyToDate = PropertyToDate
        propertyobj.PropertyStatus= PropertyStatus
        propertyobj.save()
        

        return render(request,template_name='AddProperty.html')  