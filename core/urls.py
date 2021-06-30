from django.urls.conf import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.redirect_login),
    path('accounts/login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('signin/', views.signin, name='signin'),
    path('index/', views.main_page, name='index'),
    path('service/',views.solicitar_servicio, name='service'),
    path('service/edit/<int:pk>',views.editar_solicitud, name='service_edit'),
    path('signin/phone/new/<str:user>', views.pos_signin, name='pos-signin'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('service/view', views.consultar_solicitudes, name="service_view"),
    path('service/view/staff', views.consultar_solicitudes_staff, name='service_view_staff'),
    path('contract/', views.registrar_contrato, name='contract'),
    path('contract/view/', views.consultar_contratos, name='contract_view'),
    path('contract/view/staff', views.consultar_contratos_staff, name='contract_view_staff'),
    path('pay/', views.ingresar_pago, name='pago'),
    path('causes/', views.ingresar_causas, name='ingresar_causas'),
    path('budget/', views.registrar_presupuesto, name='budget')
]