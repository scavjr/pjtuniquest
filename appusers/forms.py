
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
# from django.forms.fields import EmailField
# rom django.forms.forms import Form
# from django.contrib.auth.forms import UserCreationForm


class CadUsuarioForm(UserCreationForm):
    username = forms.CharField(label='Nome de Usuário', min_length=5, max_length=10)  
    #email = forms.EmailField(label='e-mail')
    first_name = forms.CharField(label='Primeiro Nome', min_length=5, max_length=20)
    #last_name = forms.CharField(label='Último Nome', min_length=5, max_length=150)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Senha', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control","size": "20"})
        self.fields["password1"].widget.attrs.update({"class": "form-control", "size": "15",})
        #self.fields["email"].widget.attrs.update({"class": "form-control", "size": "60",})
        self.fields["first_name"].widget.attrs.update({"class": "form-control", "size": "20",})
        #self.fields["password1"].widget.attrs.update({"class": "form-control", "size": "60",})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "size": "15",})
        #self.fields["last_name"].widget.attrs.update({"class": "form-control", "size": "60",})
  
    def username_clean(self):
        print("password username") 
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("Usuário já existe!")
        return username
  
    def email_clean(self):
        print("password custom email") 
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():  
            raise ValidationError("Email já existe")
        return email  
  
    def clean_password2(self):
        print("password custom") 
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
  
        if password1 and password2 and password1 != password2:
            raise ValidationError("Senhas não conferem")
        return password2
  
    def save(self, commit=True):  
        user = User.objects.create_user(  
            username=self.cleaned_data['username'], 
            #email=self.cleaned_data['email'],  
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            #last_name=self.cleaned_data['last_name'],
        )  
        return user  