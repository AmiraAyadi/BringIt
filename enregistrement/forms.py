from django import forms

from compte.models import Utilisateurs, Adresse
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django.forms.widgets import EmailInput




class UserForm(forms.ModelForm):

    class Meta:

        model = Utilisateurs

        fields = ('prenom','nom','email','jour_naissance','mois_naissance','annee_naissance' , 'sexe','telephone')
class AddressForm(forms.ModelForm):

    class Meta:

        model = Adresse

        fields = '__all__'




# class Enregistrement(forms.ModelForm):

#     prenom = forms.CharField(
#         label='Prénom',
#         max_length=100,
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Prénom'}),
#         required=True,
#     )
#     nom = forms.CharField(
#         label='nom',
#         max_length=100,
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nom'}),
#         required=True,
#     )
#     email = forms.EmailField(
#         label='Email',
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'autocorrect':'off',
#             'autocapitalize':'none',
#             'class':'form-control',
#             'placeholder':'Email'
#         }),
#         required=True,
#     )
#     mdp = forms.CharField(
#         label='Mot de passe',
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'type':'password',
#             'class':'form-control',
#             'placeholder':'Mot de passe'
#         }),
#         required=True,
#     )
#     mdp_validation = forms.CharField(
#         label='mot de passe validation',
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'type':'password',
#             'class':'form-control',
#             'placeholder':'Entrz votre mot de passe encore ue fois'
#         }),
#         required=True,
#     )

    	

#     #captcha = CaptchaField()

#     # Functions
#     #------------
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if email is not None and email is not '':
#             try:
#                 User.objects.get(email=email)
#                 raise forms.ValidationError("Email existe deja.")
#             except User.DoesNotExist:
#                 return email
#         else:
#             raise forms.ValidationError("ne peut etre vide!")

#     def clean_password_repeated(self):
#         password = self.cleaned_data['mdp'] # cleaned_data dictionary has the
#         # the valid fields
#         password_repeated = self.cleaned_data['mdp_validation']
#         if password != password_repeated:
#             raise forms.ValidationError("Passwords do not match.")
#         return password_repeated


# # Captcha Setup:
# # http://django-simple-captcha.readthedocs.org/en/latest/usage.html#installation
