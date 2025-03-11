from django import forms
from models import AuthUser
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = AuthUser
        fields = ('username', 'password')