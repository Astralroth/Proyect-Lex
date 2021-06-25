from django.urls.conf import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('',views.redirect_login),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('signin/', views.signin, name='signin'),
    path('index/', views.main_page, name='index'),
    path('service/',views.solicitar_servicio, name='service'),
    path('service/edit/<int:pk>',views.editar_solicitud, name='service_edit'),
    path('signin/phone/new/<str:user>', views.pos_signin, name='pos-signin'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/<str:user>', views.profile_edit, name='profile_edit'),
    path('service/view', views.consultar_solicitudes, name="service_view"),
    path('service/view/staff', views.consultar_solicitudes_staff, name='service_view_staff')
]
