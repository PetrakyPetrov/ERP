from django import forms
from django.core.validators import RegexValidator
from django.forms import CheckboxInput
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from companies.models import Company
from .models import Employee
from .models import JobPosition

numeric = RegexValidator(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', 'Невалиден номер')
numerical = RegexValidator(r'(\d)', 'Невалидно ЕГН')


class EmployeeForm(forms.ModelForm):

    SEX_TYPES = (
        ('m', 'Мъж'),
        ('f', 'Жена')
    )

    first_name = forms.CharField(label='Име', widget=forms.TextInput(attrs={'class': 'form-control'}))
    second_name = forms.CharField(label='Презиме', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    egn = forms.CharField(label='ЕГН', widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[numerical])
    date_of_birth = forms.DateField(label='Дата на раждане', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    phone_number = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}),  validators=[numeric])
    email = forms.EmailField(label='Имейл', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    sex = forms.ChoiceField(label='Пол', choices = SEX_TYPES, widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    company = job_position = forms.ModelChoiceField(label='Фирма', queryset=Company.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    job_position = forms.ModelChoiceField(label='Длъжност', queryset=JobPosition.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    salary = forms.FloatField(label='Заплата', required=False, max_value=10000, min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': "0.01"}))
    date_of_appointment = forms.DateField(label='Дата на назначаване', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    date_of_dismiss = forms.DateField(label='Дата на свобождаване', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    is_active = forms.BooleanField(label='Активен служител', required=False, widget=CheckboxInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = "__all__"
        # fields = ['name', 'phone_number', 'email', 'is_company']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if len(str(phone_number)) < 10:
            raise ValidationError('Невалиден номер')

        return phone_number

    def clean_egn(self):
        egn = self.cleaned_data['egn']

        if len(str(egn)) < 10:
            raise ValidationError('Невалидно ЕГН')

        return egn