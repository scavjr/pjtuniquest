from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import ValidationError
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class login_form(AuthenticationForm):
    username = UsernameField(
        label='Usuário',
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control","size": "20"})
        self.fields["password"].widget.attrs.update({"class": "form-control", "size": "60", "label":"dfsdf"})
        self.fields["password"].label = "Senha"
        
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(_("rwrwwerwr"), code="inactive",)
        if user.username.startswith("s"):
            raise ValidationError(_("sorry"), code="no_b_users")
        return redirect('users/cadastro_users')