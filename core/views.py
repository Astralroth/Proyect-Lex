from django.core.files.storage import FileSystemStorage
from .models import Servicio, Telefono
from django.contrib.auth.models import User
from core.forms import EditUser, SignUpForm, SolicitarServicioForm, TelefonoForm
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.

def signin(request):
    datos={
        'user':SignUpForm()
    }
    if request.method=='POST':
        formulario=SignUpForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data.get('username')
            raw_password1=formulario.cleaned_data.get('password1')
            raw_password2=formulario.cleaned_data.get('password2')
            if raw_password1==raw_password2:
                formulario.save()
                return redirect('pos-signin',user=username)
                
        if formulario.is_valid()==False:
            datos['error'] = "Datos ingresados no validos"
    return render(request,'core/signin.html',datos)

def pos_signin(request, user):
    datos={
        'form':TelefonoForm()
    }
    usuario=get_object_or_404(User,username=user)
    if request.method=='POST':
        formulario=TelefonoForm(request.POST)
        count=User.objects.filter(username=user).count()
        if count==0:
            if formulario.is_valid():
                formulario.save(usuario)
                return redirect('login')
            if formulario.is_valid()==False:
                datos['error']=formulario.errors
        else:
            datos['error']="El usuario ya tiene un telefono registrado"
    return render(request, 'core/pos_signin.html', datos)

def main_page(request):
    if request.user.is_authenticated==True:
        return render(request,'core/index.html')
    else:
        return redirect('login')

def solicitar_servicio(request):
    datos={
        'form':SolicitarServicioForm()
    }
    if request.method=='POST':
        formulario=SolicitarServicioForm(request.POST,request.FILES)
        id=User.objects.get(username=request.user.username)
        if formulario.is_valid():
            formulario.save(id)
            datos['mensaje']="Agregado correctamente"
    if request.user.is_authenticated==True:
        return render(request,'core/solicitar_servicio.html', datos)
    else:
        return redirect('login')

def redirect_login(request):
    return redirect('login')

def profile(request):
    if request.user.is_authenticated==True:
        return redirect('profile_edit', user=request.user)
    else:
        return redirect('login')

def profile_edit(request,user):
    usuario=get_object_or_404(User, username=user)
    phone=get_object_or_404(Telefono,user_id=usuario.id)
    if request.method=='POST':
       form_user=EditUser(request.POST, instance=usuario)
       form_phone=TelefonoForm(request.POST, instance=phone)
       if form_user.is_valid() and form_phone.is_valid():
           form_user.save()
           form_phone.save(usuario)
           return redirect('index')
    else:
        datos={
        'form_user':EditUser(instance=usuario),
        'form_phone':TelefonoForm(instance=phone)
    }    
    if request.user.is_authenticated==True:
        return render(request, 'core/modificar_perfil.html',datos)
    else:
        return redirect('login')

def editar_solicitud(request,pk):
    servicio=get_object_or_404(Servicio, id=pk)
    if request.method=='POST':
        form=SolicitarServicioForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
    else:
        form=SolicitarServicioForm(instance=servicio)
    if request.user.is_authenticated==True:
        return render(request, 'core/consultar_servicio.html', {'form':form})
    else:
        return redirect('login')
    
def consultar_solicitudes(request):
    user=User.objects.get(username=request.user.username)
    form=Servicio.objects.filter(cliente_id=user.id).all()
    return render(request, 'core/consultar_solicitudes.html',{'list':form})

def consultar_solicitudes_staff(request):
    service=Servicio.objects.select_related('cliente').all()
    
    return render(request, 'core/consultar_solicitudes.html',{'list':service})