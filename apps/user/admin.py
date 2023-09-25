from django.contrib import admin
from .models import User
from datetime import date

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'age_calculator',
        'phone',
        'status',
    )

    #-----------Calcular la edad-----------------------
    @admin.display(description='edad') # Cambia el nombre en el header
    def age_calculator(self, obj):
        current_date = date.today() #Declaramos el tiempo actual.

        if obj.birthdate == None: #Validar si no tiene la fecha de nacimiento cargada.
            age = 'S/F Nacimiento'
        else:
            age = current_date.year - obj.birthdate.year #Se le resta al año actual, el año de nacimiento de la persona.
            if (current_date.month, current_date.day) < (obj.birthdate.month, obj.birthdate.day):#Validación de cumpleaños, si todavia no cumplio años en el año actual se descuenta un año.
                age = current_date.year - obj.birthdate.year - 1

        return age
    #--------------------------------------------------
    
    age_calculator.admin_order_field = 'birthdate' # Permite ordenar por edad
    search_fields = ('last_name',) # Barra de busqueda por apellido.
    list_filter = ['status',] # Filtro de busqueda por trabajo.


admin.site.register(User, UserAdmin)
