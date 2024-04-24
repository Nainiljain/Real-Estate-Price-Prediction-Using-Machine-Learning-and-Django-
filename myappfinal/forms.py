from django import forms

class RatechangePredictionForm(forms.Form):
    SrNo = forms.IntegerField(label='Sr No', min_value=0)
    PropertyCategory = forms.ChoiceField(widget = forms.Select(), 
    choices = ([('0','Residential'), ('1','Commercial')]), initial='3', required = True,)
    ResdentialType = forms.ChoiceField(widget = forms.Select(), 
    choices = ([('0','Flate'), ('1','House'),('2','None')]), initial='3', required = True,)
    CommercialType = forms.ChoiceField(widget = forms.Select(), 
    choices = ([('0','Office'), ('1','Shop/Showrrom'),('2','Plot'),('3','None')]), initial='4', required = True,)
    AreaSize = forms.IntegerField(label='AreaSize', min_value=0)
    Luxury = forms.ChoiceField(widget = forms.Select(), 
    choices = ([('0','Yes'), ('1','No')]), initial='3', required = True,)
    PropertyLocation = forms.ChoiceField(widget = forms.Select(), 
    choices = ([('0','Incity'), ('1','Suburb')]), initial='3', required = True,)
    PropertyAge = forms.ChoiceField(widget = forms.Select(), 
    choices = ([('0','Old'), ('1','New')]), initial='3', required = True,)
    NoofAmenitities = forms.IntegerField(label='No of Amenitities', min_value=0)
    SubCategory = forms.ChoiceField(widget = forms.Select(), 
    choices = ([('0','1bhk'), ('1','2bhk'),('2','3bhk'),('3','4bhk'),('4','5bhk'),('5','None')]), initial='6', required = True,)
    PriceFtRange = forms.IntegerField(label='PriceFtRange', min_value=0)
    RentUnrent = forms.ChoiceField(label='Rent/Purchase', widget = forms.Select(), 
    choices = ([('0','Rent'), ('1','Purchase')]), initial='3', required = True  )

