from django.forms import ModelForm
from django import forms
from products.models import Review,  DetailInfo, Footwears

class DetailInfoForm(forms.ModelForm):
    class Meta:
        model = DetailInfo
        fields = ['first_name']

class AddReviewForm(ModelForm):
    star_given = forms.IntegerField(max_value=5, min_value=0)
    class Meta:
        model = Review
        fields = ['comment', 'star_given']


class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']


class FootwearForm(forms.ModelForm):
    class Meta:
        model = Footwears
        fields = ['name', 'price','image']