from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class State(models.Model):
    StateName =models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.StateName

class City(models.Model):
    CityName =models.CharField(max_length=30)
    State=models.ForeignKey(State, on_delete=models.CASCADE)
  
    def __str__(self) -> str:
        return self.CityName    

class Area(models.Model):
    AreaName=models.CharField(max_length=30)
    City=models.ForeignKey(City,  on_delete=models.CASCADE)
    State=models.ForeignKey(State, on_delete=models.CASCADE)
  
    def __str__(self) -> str:
        return self.AreaName

class Features(models.Model):
    FeaturesName =models.CharField(max_length=30)
    Featurestitle =models.CharField(max_length=30)
    Featuresdetails =models.TextField(max_length=80) 
    
    def __str__(self) -> str:
        return self.FeaturesName
    def __str__(self) -> str:
        return self.Featurestitle
    def __str__(self) -> str:
        return self.Featuresdetails    

class Category(models.Model):
    CategoryName =models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.CategoryName
    
class Subcategory(models.Model):
    SubcategoryName =models.CharField(max_length=30)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.SubcategoryName

class Property(models.Model):
    PropertyName =models.CharField(max_length=30)
    User =models.ForeignKey(User,null=True, blank=True, default = None, on_delete=models.CASCADE)
    Area=models.ForeignKey(Area, on_delete=models.CASCADE)
    Subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    PropertyTitle = models.CharField(max_length=30,default='Property')
    PropertySellorRent =models.CharField(max_length=30,default='Sell')
    PropertyAmount =models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    PropertyFromDate =models.DateTimeField(default=datetime.now(), blank=True)
    PropertyImage =models.ImageField(upload_to='images')
    PropertyToDate =models.DateTimeField(default=datetime.now(), blank=True)
    PropertyStatus =models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.PropertyName
    def __str__(self) -> str:
        return self.PropertyTitle
    def __str__(self) -> str:
        return self.PropertySellorRent
    def __str__(self) -> str:
        return self.PropertyAmount
    def __str__(self) -> str:
        return self.PropertyFromDate
    def __str__(self) -> str:
        return self.PropertyImage
    def __str__(self) -> str:
        return self.PropertyToDate
    def __str__(self) -> str:
        return self.PropertyStatus

class Requirements(models.Model):
    Area =models.ForeignKey(Area,null=True, blank=True, default = None, on_delete=models.CASCADE)
    Subcategory =models.ForeignKey(Subcategory,null=True, blank=True, default = None, on_delete=models.CASCADE)
    RequirementsBudget = models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    RequirementsBuyorRent = models.CharField(max_length=30,default='Buy')
    RequirementsRemarks = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.RequirementsBudget
    def __str__(self) -> str:
        return self.RequirementsBuyorRent
    def __str__(self) -> str:
        return self.RequirementsRemarks