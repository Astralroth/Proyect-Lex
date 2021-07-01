from .models import Contrato, Servicio, Telefono
from django.contrib.auth.models import Group, User
from core.forms import AgregarCausas, ContratoForm, EditUser, PagosForm, PresupuestoForm, SignUpForm, SolicitarServicioForm, TelefonoForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
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
                group=Group.objects.get_or_create(name='cliente')
                user=User.objects.get(username=username)
                user.groups.add(group[0])
                if user.get_group_permissions()==set():
                    permissions={25,26,28,29,30,32,16,14}
                    group[0].permissions.set(permissions)
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
        count=Telefono.objects.filter(user_id=usuario).count()
        if count==0:
            if formulario.is_valid():
                formulario.save(usuario)
                return redirect('login')
            if formulario.is_valid()==False:
                datos['error']=formulario.errors
        else:
            datos['error']="El usuario ya tiene un telefono registrado"
    return render(request, 'core/pos_signin.html', datos)

@login_required
def main_page(request):
    return render(request,'core/index.html')

@login_required
@permission_required('core.add_servicio')
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

@login_required
@permission_required('auth.change_user')
def profile_edit(request):
    usuario=get_object_or_404(User, username=request.user.username)
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
    return render(request, 'core/modificar_perfil.html',datos)

@login_required
@permission_required('core.change_servicio')
def editar_solicitud(request,pk):
    servicio=get_object_or_404(Servicio, id=pk)
    if request.method=='POST':
        form=SolicitarServicioForm(request.POST, request.FILES, instance=servicio)
        id=User.objects.get(username=servicio.cliente)
        if form.is_valid():
            form.save(id)
            return redirect('service_view')
    else:
        datos={
            'form':SolicitarServicioForm(instance=servicio)
        }
    return render(request, 'core/solicitar_servicio.html', datos)

@login_required
@permission_required('core.view_servicio')
def consultar_solicitudes(request):
    user=User.objects.get(username=request.user.username)
    form=Servicio.objects.filter(cliente_id=user.id).all()
    return render(request, 'core/consultar_solicitudes.html',{'list':form})

@login_required
def consultar_solicitudes_staff(request):
    service=Servicio.objects.select_related('cliente').all()
    return render(request, 'core/consultar_solicitudes.html',{'list':service})

@permission_required('core.add_contrato')
def registrar_contrato(request):
    datos={
        'form':ContratoForm()
    }
    if request.method=="POST":
        form=ContratoForm(request.POST, request.FILES)
        id=User.objects.get(username=request.user.username)
        if form.is_valid():
            form.save(id)
            datos['mensaje']="Agregado correctamente"
        if form.is_valid()==False:
            datos['mensaje']=form.errors
        
    return render(request, 'core/registrar_contrato.html',datos)

@permission_required('core.view_contrato')
def consultar_contratos(request):
    user=User.objects.get(username=request.user.username)
    form=Contrato.objects.filter(abogado_id=user.id).all()
    return render(request, 'core/consultar_contratos.html', {'list':form})

def consultar_contratos_staff(request):
    contrato=Contrato.objects.select_related('abogado').all()
    return render(request, 'core/consultar_contratos.html',{'list':contrato})

@permission_required('add_pago')
def ingresar_pago(request):
    datos={
        'form':PagosForm()
    }
    if request.method=='POST':
        formulario=PagosForm(request.POST)
        id=User.objects.get(username=request.user.username)
        if formulario.is_valid():
            formulario.save(id)
            datos['mensaje']="Agregado correctamente"
        if formulario.is_valid()==False:
            datos['mensaje']=formulario.errors
    
    return render(request,'core/ingresar_pago.html', datos)

@login_required
@permission_required('core.add_causa')
def ingresar_causas(request):
    datos={
        'form':AgregarCausas()
    }
    if request.method=='POST':
        formulario=AgregarCausas(request.POST)
        id=User.objects.get(username=request.user.username)
        if formulario.is_valid():
            formulario.save(id)
            datos['mensaje']="Guardado Exitosamente"
        if formulario.is_valid()==False:
            datos['mensaje']=formulario.errors
    return render(request, 'core/ingresar_causa.html', datos)

def registrar_presupuesto(request):
    datos={
            'form':PresupuestoForm()
        }
    if request.method=="POST":
        form=PresupuestoForm(request.POST, request.FILES)
        id=User.objects.get(username=request.user.username)
        if form.is_valid():
            form.save(id)   
    return render(request, 'core/registrar_presupuesto.html',datos)

