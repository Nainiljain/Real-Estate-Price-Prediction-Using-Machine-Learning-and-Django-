from django import forms

class PricePredictionForm(forms.Form):
    PropertyCategory = forms.IntegerField(label='Property Category', min_value=0)
    ResdentialType = forms.IntegerField(label='Resdential Type', min_value=0)
    CommercialType = forms.IntegerField(label='Commercial Type', min_value=0)
    AreaSize = forms.IntegerField(label='AreaSize', min_value=0)
    Luxury = forms.IntegerField(label='Luxury', min_value=0)
    PropertyLocation = forms.IntegerField(label='Property Location', min_value=0)
    PropertyAge = forms.IntegerField(label='Property Age', min_value=0)
    NoofAmenitities = forms.IntegerField(label='No of Amenitities', min_value=1)
    SubCategory = forms.IntegerField(label='Sub Category', min_value=0)
    PriceFtRange = forms.IntegerField(label='PriceFtRange', min_value=0)
    RentUnrent = forms.IntegerField(label='RentUnrent', min_value=0)