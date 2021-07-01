from django.contrib.auth.models import User
from core.models import Causa, Contrato, Pago, Presupuesto, Servicio, Telefono
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
    files=forms.FileField(required=False)
    
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
    files_boleta=forms.FileField(required=False)
    files_causa=forms.FileField(required=False)
    datetime=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    type_service=forms.ChoiceField(choices=(('',''),('Familia','Familia'),('Civiles','Civiles'),('Inmobiliarias','Inmobiliarias'),('Salud','Salud'),('Transito','Transito'),),widget=forms.Select(attrs={'class':'form-control'}))
    additional_service=forms.ChoiceField(choices=(('',''),('Otros','Otros'),),required=False, widget=forms.Select(attrs={'class':'form-control'}))
    # format=forms.ChoiceField(choices=(('word','word'),('pdf','pdf')),widget=forms.RadioSelect(),required=False)
    class Meta:
        model = Contrato
        fields = ("name","rut","age","email","phone","files_boleta","files_causa","datetime", "type_service", "additional_service",)
    
    def save(self,id,commit=True):
        user=super(ContratoForm,self).save(commit=False)
        if commit:
            user.set_id(id)
            user.save()
        return user

class PagosForm(forms.ModelForm):

    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Cliente '}))
    rut=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rut'}), label="Rut")
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Fecha','type':'date'}))
    type=forms.ChoiceField(choices=(('',''),('Efectivo','Efectivo'),('Transferencia','Transferencia'),('Cheque','Cheque'),('Crédito','Crédito'),('Débito','Débito'),),widget=forms.Select(attrs={'class':'form-control'}))
    mount=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Monto '}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email '}))

    class Meta:
        model = Pago
        fields = ("name","rut","date","type","mount","email",)
        
    def save(self,id,commit=True):
        user= super(PagosForm, self).save(commit=False)
        if commit:
            user.set_id(id)
            user.save()
        return user

class AgregarCausas(forms.ModelForm):

    name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Cliente'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Edad'}))
    email=forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    phone=forms.CharField(max_length=12, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Teléfono'}))
    rut=forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rut'}))
    files_boleta=forms.FileField(widget=forms.FileInput, label="Boleta",required=False)
    files_causa=forms.FileField(widget=forms.FileInput, label="Causa", required=False)
    files_contrato=forms.FileField(widget=forms.FileInput, label="Contrato",required=False)
    
    class Meta:
        model = Causa
        fields = ("name", "age", "email", "phone", "rut","files_boleta","files_causa", "files_contrato",)
    
    def save(self,id,commit=True):
        user= super(AgregarCausas, self).save(commit=False)
        if commit:
            user.set_id(id)
            user.save()
        return user

class PresupuestoForm(forms.ModelForm):
    
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Cliente'}))
    servicio=forms.ChoiceField(choices=(('',''),('Familia','Familia'),('Civiles','Civiles'),('Inmobiliarias','Inmobiliarias'),('Salud','Salud'),('Transito','Transito'),),widget=forms.Select(attrs={'class':'form-control'}))
    presupuesto=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Presupuesto'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    rut=forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Rut'}))
    
    class Meta:
        model = Presupuesto
        fields = ("name", "servicio", "presupuesto", "email","rut",)
        
    
    def save(self,id,commit=True):
        user=super(PresupuestoForm,self).save(commit=False)
        if commit:
            user.set_id(id)
            user.save()
        return user