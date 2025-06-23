from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import administration, product

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",
                  "password1", "password2", "is_staff")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class AdminForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['product_name', 'product_price', 'product_description']
        labels = {
            'product_name': 'Product Name',
            'product_price': 'Product Price',
            'product_description': 'Product Description',
        }
        widgets = {
            'product_description': forms.Textarea(attrs={'rows': 4}),
        }





