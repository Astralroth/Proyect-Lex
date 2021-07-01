# from core.models import User
from core.models import Causa, Contrato, Pago, Presupuesto, Servicio, Telefono
from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

# @admin.register(Servicio)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['cliente','first_name' ,'age', 'email','phone']
#     list_filter = ['age']
#     ordering=['phone']
    
#     fieldsets = (
#         (None, {
#             'fields': ('cliente','age')
#         }),
#         ('Availability', {
#             'fields': ('cause', 'files')
#         }),
#     )
#     add_fieldsets=(
#         (None, {
#             'classes': ('wide',),
#             'fields':('cliente','email'),
#         })
#     )

admin.site.register(Telefono)
admin.site.register(Servicio)
admin.site.register(Pago)
admin.site.register(Presupuesto)
admin.site.register(Causa)
admin.site.register(Contrato)