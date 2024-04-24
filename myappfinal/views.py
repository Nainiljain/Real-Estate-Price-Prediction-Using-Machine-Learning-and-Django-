from django.http import HttpResponse
import os
import pickle
import numpy as np
from django.shortcuts import render 
from .models import Property
from .models import Area
from .models import Category
from .forms import RatechangePredictionForm
from .models import Contactform
# Create your views here.
def rate_change(request):
    #return HttpResponse
    print(request)
    if request.method == 'POST':
        srno = float(request.POST.get("number"))
        category = float(request.POST.get("opr"))
        residentialtype = float(request.POST.get("residential")) 
        commercialtype = request.POST.get("commercial")
        size = float(request.POST.get("size"))
        Luxury = float(request.POST.get("luxury"))
        location = float(request.POST.get("location"))
        subcategory = float(request.POST.get("category"))
        Age = float(request.POST.get("Age"))
        Ameneties = float(request.POST.get("Ameneties"))
        pice = float(request.POST.get("price"))
        choice = float(request.POST.get("choice"))
        print(srno)
        print(category)
        print(residentialtype)
        print(commercialtype)
        print(size)
        print(Luxury)
        print(location)
        print(subcategory)
        print(Age)
        print(Ameneties)
        print(pice)
        print(choice)
        form = RatechangePredictionForm(request.POST)
      
        list=[srno,category,residentialtype,commercialtype,size,Luxury,location,subcategory,Age,Ameneties,pice,choice]
        with open('classifierforrent.pkl','rb') as file:
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
    if request.POST !=None:
        name=request.POST.get("Name")
        email = request.POST.get("Email")
        subject = request.POST.get("Subject")
        message = request.POST.get("Message")
        contactobj = Contactform()
        contactobj.name = name
        contactobj.email = email
        contactobj.subject = subject
        contactobj.message= message
        print(contactobj)
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
    return render(request,template_name='AddProperty.html')