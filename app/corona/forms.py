from django import forms

class PatientRegisterForm(forms.Form):
    name = forms.CharField(label='Jmeno', required=True)
    surname = forms.CharField(label='Prijmeni', required=True)
    birthid = forms.IntegerField(label='Rodne cislo', required=True)
    email = forms.CharField(label='Email', required=True)
    phone = forms.CharField(label='Telefonni cislo', required=True)
    address = forms.CharField(label='Adresa', required=True)
