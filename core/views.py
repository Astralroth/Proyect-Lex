from core.models import Users
from core.forms import SignUpForm
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def login(request):
    datos={
        'form':AuthenticationForm()
    }
    return render(request,'core/login.html',datos)

def logout(request):
    return render(request,'core/logout.html')

def signin(request):
    datos={
        'form':SignUpForm()
    }
    if request.method=='POST':
        formulario=SignUpForm(request.POST)
        if formulario.is_valid():
            username= formulario.cleaned_data.get('username')
            raw_password1=formulario.cleaned_data.get('password1')
            raw_password2=formulario.cleaned_data.get('password2')
            if raw_password1==raw_password2:
                formulario.save()
                return redirect('login')
                
        if formulario.is_valid()==False:
            datos['error'] = "Datos ingresados no validos"
    return render(request,'core/signin.html',datos)
def main_page(request):
    return render(request,'core/index.html')

def redirect_login(request):
    return redirect('login')