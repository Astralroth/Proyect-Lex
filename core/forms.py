from django.contrib.auth.models import User
from core.models import Causas, Contrato, Pagos, Presupuesto, Servicio, Telefono
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
    
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del cliente'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Edad'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo electronico'}))
    phone=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefono celular'}))
    cause=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','style':'height: 80px','placeholder':'Redactar causa'}))
    files=forms.FileField()
    
    class Meta:
        model = Servicio
        fields = ("first_name", "age", "email", "phone", "cause", "files",)
        
    def save(self,id,commit=True):
        user= super(SolicitarServicioForm, self).save(commit=False)
        if commit:
            user.set_id(id)
            user.save()
        return user
        
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
        
class ContratoForm(forms.ModelForm):
    
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}))
    rut=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rut'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Edad'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo electronico'}))
    phone=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefono celular'}))
    files_boleta=forms.FileField(widget=forms.FileInput, required=False)
    files_causa=forms.FileField(widget=forms.FileInput, required=False)
    datetime=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    type_service=forms.ChoiceField(choices=(('',''),('Familia','Familia'),('Civiles','Civiles'),('Inmobiliarias','Inmobiliarias'),('Salud','Salud'),('Transito','Transito'),),widget=forms.Select(attrs={'class':'form-control'}))
    additional_service=forms.ChoiceField(choices=(('',''),('Otros','Otros'),),widget=forms.Select(attrs={'class':'form-control'}))
    format=forms.ChoiceField(choices=(('word','word'),('pdf','pdf')),widget=forms.RadioSelect())
    class Meta:
        model = Contrato
        fields = ("name","rut","age","email","phone","files_boleta","files_causa","datetime",)
    
    def save(self,id,commit=True):
        user=super(ContratoForm,self).save(commit=False)
        if commit:
            user.set_id(id)
            user.save()
        return user

class PagosForm(forms.ModelForm):

    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre del cliente")
    rut=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Rut")
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}), label="Fecha")
    type=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Tipo de pago")
    mount=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="Monto")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label="Correo electronico")

    class Meta:
        model = Pagos
        fields = ("name","rut","date","type","mount","email",)

    def save(self,id,commit=True):
        user= super(PagosForm, self).save(commit=False)
        if commit:
            user.set_id(id)
            user.save()
        return user

class AgregarCausas(forms.ModelForm):

    name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre del cliente")
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="Edad")
    email=forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class':'form-control'}),label="Correo electronico")
    phone=forms.CharField(max_length=12, widget=forms.NumberInput(attrs={'class':'form-control'}), label="Telefono celular")
    rut=forms. CharField(max_length=10, widget=forms.NumberInput(attrs={'class':'form-control'}), label="Rut")
    files_boleta=forms.FileField(widget=forms.FileInput, label="Boleta")
    files_causa=forms.FileField(widget=forms.FileInput, label="Causa")
    files_contrato=forms.FileField(widget=forms.FileInput, label="Contrato")
    
    class Meta:
        model = Causas
        fields = ("name", "age", "email", "phone", "rut","files_boleta","files_causa", "files_contrato",)

class PresupuestoForm(forms.ModelForm):
    
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre del cliente")
    servicio=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Tipo Servicio")
    presupuesto=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label="Presupuesto")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label="Correo Electrónico")
    
    
    class Meta:
        model = Presupuesto
        fields = ("first_name", "servicio", "presupuesto", "email",)
        
    
    def save(self,id,commit=True):
        user=super(PresupuestoForm,self).save(commit=False)
        if commit:
            user.set_id(id)
            user.save()
        return user