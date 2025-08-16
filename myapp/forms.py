from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Stuff

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)



class StuffForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ['stuff_name', 'price', 'stuff_description', 'photo', 'rate']
        labels = {
            'stuff_name': 'Stuff Name',
            'price': 'Price',
            'stuff_description': 'Stuff Description',
            'photo': 'Photo',
            'rate': 'Rate'
        }
        widgets = {
            'stuff_description': forms.Textarea(attrs={'rows': 4}),
            'rate': forms.Select(choices=[(i,i) for i in range(1, 11)])
        }






