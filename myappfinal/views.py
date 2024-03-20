from django.http import HttpResponse
from django.shortcuts import render 
from .models import Property
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
    properties = Property.objects.filter(PropertyName__in =['showroom','House','shop','villa','plot','Gaming studio','Tree house']).values()
    context = {'properties': properties}
    return render(request,'index.html',context)
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