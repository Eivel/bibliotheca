from django.forms import ModelForm
from bibliotheca.models import Readers
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ReadersForm(ModelForm):
    address_street = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz ulicę'}), label="Ulica")

    address_strno = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Wpisz numer domu', 'value': '', 'min': 1, 'step': 1}),
        label="Nr domu")

    address_aptno = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Wpisz numer mieszkania', 'value': '', 'min': 1, 'step': 1}),
        label="Nr mieszkania", required=False)

    address_postcode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz kod pocztowy'}),
        label="Kod pocztowy", max_length=7)

    address_city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz miasto'}), label="Miasto",
        max_length=7)

    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz numer telefonu'}),
        label="Nr telefonu", max_length=12)

    class Meta:
        model = Readers
        fields = ['address_street', 'address_strno', 'address_aptno', 'address_postcode', 'address_city',
                  'phone_number']


class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz nazwę użytkownika'}),
        label="Login")
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz hasło'}), label="Hasło")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz hasło ponownie'}),
        label="Powtórz hasło")
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz adres email'}), label="Adres email")
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz imię'}), label="Imię")
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz nazwisko'}), label="Nazwisko")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user