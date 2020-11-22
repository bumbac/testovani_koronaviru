from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Uzivatelske jmeno', required=True)
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput, required=True)


class PatientRegisterForm(forms.Form):
    username = forms.CharField(label='Uzivatelske jmeno', required=True)
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput, required=True)
    name = forms.CharField(label='Jmeno', required=True)
    surname = forms.CharField(label='Prijmeni', required=True)
    birthid = forms.IntegerField(label='Rodne cislo', required=True)
    email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Telefonni cislo', required=True)
    address = forms.CharField(label='Adresa', required=True)