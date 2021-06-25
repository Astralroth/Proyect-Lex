# from core.models import User
from core.models import Servicio, Telefono
from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'last_login','id']
#     list_filter = ['last_login']
#     ordering=['id']
    
#     fieldsets = (
#         (None, {
#             'fields': ('username','email','groups')
#         }),
#         ('Availability', {
#             'fields': ('last_login', 'date_joined')
#         }),
#     )
#     add_fieldsets=(
#         (None, {
#             'classes': ('wide',),
#             'fields':('username','email','user_permissions','groups'),
#         })
#     )

admin.site.register(Telefono)
admin.site.register(Servicio)