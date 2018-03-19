from django import forms
from django.forms import ModelForm

from .models import Brand, Medicine, Bandage

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        labels = {
            'name': 'Producent',
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Kategoria',
        }


class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = '__all__'
        labels = {
            'name': 'Rodzaj',
        }

class MedicineForm(ModelForm):
    name  = forms.CharField(label='Nazwa', max_length=500)
    category = forms.SelectMultiple(label='Kategoria')
    type = forms.Select(empty_label='Forma leku')
    brand = forms.Select(empty_label='Producent')
    quantity = forms.CharField(max_length=500)
    date = forms.DateField()
    description = forms.CharField(max_length=1500)
    link = forms.CharField(max_length=500)


class BandageForm(ModelForm):
    name = forms.CharField(max_length=500)
    brand = forms.Select(empty_label='Producent')
    quantity = forms.IntegerField()
    date = forms.DateField()
    description = forms.CharField(max_length=1500)
    link = forms.CharField(max_length=500)



