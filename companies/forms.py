from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import CheckboxInput

from .models import Company

numeric = RegexValidator(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', 'Невалиден номер')
vatIdn = RegexValidator(r'[A-aZ-z,0-9]', 'Невалиден номер')

class CompanyForm(forms.ModelForm):

    name = forms.CharField(label='Име', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mrp = forms.CharField(label='МОЛ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    vat = forms.CharField(label='БУЛСТАТ', widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[vatIdn])
    idn = forms.CharField(label='ЕИК', widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[vatIdn])
    city = forms.CharField(label='Град', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Имейл', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[numeric])
    parent_company = forms.ModelChoiceField(label='Подфирма на', queryset=Company.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(label='Активна фирма', required=False, widget=CheckboxInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Company
        fields = "__all__"
        # fields = ['name', 'phone_number', 'email', 'is_company']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if len(str(phone_number)) < 10:
            raise ValidationError('Невалиден номер')

        return phone_number

    def clean_vat(self):
        vat = self.cleaned_data['vat']

        if len(str(vat)) == 9 or len(str(vat)) == 13:
            return vat

        raise ValidationError('Невалиден номер')

    def clean_idn(self):
        idn = self.cleaned_data['idn']

        if len(str(idn)) == 9 or len(str(idn)) == 13:
            return idn

        raise ValidationError('Невалиден номер')