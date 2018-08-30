from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import CheckboxInput
from django.utils.translation import ugettext_lazy as _


from .models import Contact

numeric = RegexValidator(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', 'Невалиден номер')

class ContactForm(forms.ModelForm):

    name = forms.CharField(label='Име', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Телефон',widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[numeric])
    email = forms.EmailField(label='Имейл', widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    is_company = forms.BooleanField(
        label='Фирма',
        required=False,
        widget=CheckboxInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ['name', 'phone_number', 'email', 'is_company']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if len(str(phone_number)) < 10:
            raise ValidationError('Невалиден номер')

        return phone_number