from core.models import Users
from django.urls.conf import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('',views.redirect_login),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('signin/', views.signin, name='signin'),
    path('index/', views.main_page, name='index')
]
