from django.contrib.auth.models import User
from core.models import Servicio, Telefono
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=150,help_text='Requerido. 150 carácteres como máximo. Únicamente letras, dígitos y @/./+/-/_', widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre de usuario")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=forms.EmailInput(attrs={'class':'form-control'}),label="Correo electronico")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirmar contraseña", help_text="Ingresa la misma contraseña de arriba, para verificar.",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SolicitarServicioForm(forms.ModelForm):
    
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre del cliente")
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="Edad")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label="Correo electronico")
    phone=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="Telefono celular")
    cause=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'height: 80px'}), label="Redactar causa")
    
    class Meta:
        model = Servicio
        fields = ("first_name", "age", "email", "phone", "cause", "files")
        
class TelefonoForm(forms.ModelForm):
    
    phone = forms.CharField(max_length=11, widget=forms.NumberInput(attrs={'class':'form-control'}), label="Telefono")
    
    class Meta:
        model = Telefono
        fields = ("phone",)

        
    def save(self,id,commit=True):
        user=super(TelefonoForm,self).save(commit=False)
        if commit:
            user.set_id(id)
            user.save()
        return user
        
class EditUser(forms.ModelForm):
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre")
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), label="Correo electronico")
    
    class Meta:
        model = User
        fields = ("username","email",)
        
