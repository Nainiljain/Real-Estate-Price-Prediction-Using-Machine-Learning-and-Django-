"""
URL configuration for realestatefinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myappfinal import views
admin.site.site_header="Nainil Jain"
admin.site.site_title ="Nainil" 
admin.site.index_title = "Nainil title"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('about.html',views.index, name="about"),
    path('contact.html',views.index, name="contact"),
    path('error.html',views.index, name="error"),
    path('propertyagent.html',views.index, name="propertyagent"),
    path('propertylist.html',views.index, name="propertylist"),
    path('propertytype.html',views.index, name="propertytype"),
    path('testimonial.html',views.index, name="testimonial"),
    path('property',views.property, name="property"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
