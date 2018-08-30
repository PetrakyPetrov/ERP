from django import forms
from django.core.validators import RegexValidator
from django.forms import CheckboxInput

from companies.models import Company
from .models import Vehicle

numeric = RegexValidator(r'[A-aZ-z,0-9]', 'Невалидни данни')

class VehicleForm(forms.ModelForm):

    FUEL_TYPES = (
        ('d', 'Дизел'),
        ('g', 'Бензин')
    )

    license_plate = forms.CharField(label='Рег. номер', widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[numeric])
    manufacturer = forms.CharField(label='Производител', widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[numeric])
    model = forms.CharField(label='Марка/Модел', widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[numeric])
    purchase_date = forms.DateField(label='Дата на закопуване', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    warranty_end_date = forms.DateField(label='Валидна гаранция до', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    company_owner = forms.ModelChoiceField(label='Фирма', queryset=Company.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    fuel_type = forms.ChoiceField(label='Гориво', choices=FUEL_TYPES, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    is_active = forms.BooleanField(label='Активно МПС', required=False, widget=CheckboxInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Vehicle
        fields = "__all__"
        # fields = ['name', 'phone_number', 'email', 'is_company']