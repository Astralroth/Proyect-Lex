from core.models import Users
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=forms.EmailInput,label="Correo electronico")
    phone = forms.CharField(max_length=11, widget=forms.NumberInput, label="Telefono")
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", help_text="Enter the same password as above, for verification.",widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('username', 'email', 'password1', 'password2', 'phone')