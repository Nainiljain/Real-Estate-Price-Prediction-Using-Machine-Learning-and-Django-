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
    if request.method == 'POST':
        form = RatechangePredictionForm(request.POST)
        if form.is_valid():
            # Load the trained linear regression model
            
            with open('classifierforrent.pkl','rb') as file:
                clf = pickle.load(file)   
            
            # Extract input data from the form
            new_data = np.array(list(form.cleaned_data.values())).reshape(1, -1)

            # Perform prediction
            rate_change = clf.predict(new_data)[0]

            # Prepare the response  
            context = {
                'form': form,
                'rate_change': round(rate_change, 2),
            }
            return render(request, 'prediction.html', context)
    else:
        form = RatechangePredictionForm()

    context = {'form': form}
    return render(request, 'index.html', context)
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