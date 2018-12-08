from django.contrib import admin
from mylocalproject.models import (Persona, Institucion, Especialista, Evento, Voluntario, Benefactor, Practicante,
                                   Asistencia)


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):

    search_fields = ['nombres', 'apellidos', 'telefono', 'direccion', 'fecha_nacimiento']
    list_filter = ['nombres', 'apellidos']
    list_display = ('nombres', 'apellidos', 'telefono', 'direccion', 'fecha_nacimiento')

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):

    search_fields = ['nombre', 'direccion', 'contacto']
    list_display = ['nombre', 'direccion', 'contacto']
    list_filter = ['nombre']

@admin.register(Especialista)
class EspecialistaAdmin(admin.ModelAdmin):

    search_fields = ['id_persona', 'especialidad', 'activo']
    list_display = ['id_persona', 'especialidad', 'activo']
    list_filter = ['id_persona', 'especialidad', 'activo']
    list_editable = ['activo']


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):

    search_fields = ['nombre', 'lugar', 'fecha']
    list_display = ['nombre', 'lugar', 'fecha']
    list_filter = ['nombre', 'lugar', 'fecha']

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):

    search_fields = ['id_persona', 'fecha_visita', 'activo', 'evento']
    list_display = ['id_persona', 'fecha_visita', 'activo', 'evento']
    list_filter = ['id_persona', 'fecha_visita', 'activo', 'evento']
    list_editable = ['activo']

@admin.register(Benefactor)
class BenefactorAdmin(admin.ModelAdmin):

    search_fields = ['id_persona', 'encargado', 'activo']
    list_display = ['id_persona', 'encargado', 'activo']
    list_filter = ['id_persona', 'encargado', 'activo']
    list_editable = ['activo']

@admin.register(Practicante)
class PracticanteAdmin(admin.ModelAdmin):

    search_fields = ['id_persona', 'programa', 'activo']
    list_display = ['id_persona', 'programa', 'activo']
    list_filter = ['id_persona', 'programa', 'activo']
    list_editable = ['activo']

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):

    search_fields = ['id_evento', 'id_persona', 'asistio']
    list_display = ['id_evento', 'id_persona', 'asistio']
    list_filter = ['id_evento', 'id_persona', 'asistio']
    list_editable = ['asistio']
