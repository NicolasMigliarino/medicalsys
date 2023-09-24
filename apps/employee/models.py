from django.db import models
from apps.departament.models import Departament


# Create your models here.

class Employee(models.Model):
    
    #Tipos de trabajo
    JOBS_CHOICES = (
        ('0', 'Pediatra'),
        ('1', 'Cirujia'),
        ('2', 'Clinica'),
        ('3', 'Urologia'),
        ('4', 'Otros'),
    )

    #Tipo de genero.
    SEX_CHOICES = (
        ('0', 'Masculino'),
        ('1', 'Femenino'),
        ('3', 'Otro')
    )


    first_name = models.CharField('Nombre', max_length=45)
    last_name = models.CharField('Apellido', max_length=40)
    birthdate = models.DateField('Fecha de nacimiento', null=True)
    phone = models.CharField('Telefono', max_length=10, blank=True, null=True)
    sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES)
    email = models.EmailField('Email', max_length=45, blank=True, null=True)
    dni = models.CharField('DNI',max_length=8, unique=True)
    job = models.CharField('Puesto', max_length=1, choices=JOBS_CHOICES)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name='Departamento', default=None) # Relación 1 a Muchos.
    #skill = models.ManyToManyField(Skills, verbose_name='Habilidades') # Relación Muchos a Muchos
    status = models.BooleanField('Inactivo', default=False)

    class Meta:
        verbose_name = 'Empleados'
        verbose_name_plural = 'Registro de empleados'

    def __str__(self):
        return 'Especialidad:'+ str(self.get_job_display()) + ' | ' + self.first_name + ' ' + self.last_name
    

class Shifts(models.Model):
    SHIFTS_CHOICES = (
        ('0', '8:00'),
        ('1', '8:30'),
        ('2', '9:00'),
        ('3', '10:00'),
        ('4', '11:00'),
    )

    dni = models.CharField('DNI del Paciente', max_length=8) # blank=True/null=True <- no es obligatorio llenar un campo de texto.
    date = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    time = models.CharField('Horario', max_length=1, choices=SHIFTS_CHOICES)
    employee = models.ManyToManyField(Employee, verbose_name='Especilista')

    


    class Meta:
        verbose_name = 'Turnos'
        verbose_name_plural = 'Registro de Turnos'

