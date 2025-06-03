from django import forms
from django.contrib.auth.models import User

class NameForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter the password'}))
    question = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter the question'}))
    answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter the answer'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        if User.objects.filter(username=name).exists():
            raise forms.ValidationError('This username already exists')
        return name
    
class UserForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')
        if User.objects.filter(username=name).exists():
                user = User.objects.get(username=name)
                if not user.check_password(password):
                    raise forms.ValidationError('Password error')
        else:
            raise forms.ValidationError('User not found')
        return cleaned_data
    
class ResetForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        if not User.objects.filter(username=name).exists():
            raise forms.ValidationError("This username doesn't exists")
        return name
    
class ChangePasswordForm(forms.Form):
    answer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter the answer'}))
    password = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter new password'}))