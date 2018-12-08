from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Institucion(models.Model):

    nombre = models.CharField(max_length=500, blank=False, null=False)
    direccion = models.CharField(max_length=500, blank=False, null=False)
    contacto = models.CharField(max_length=500, blank=False, null=False)

    class Meta:
        unique_together = ('nombre', 'direccion')

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre


class Persona(models.Model):

    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, blank=False, null=True)
    nombres = models.CharField(max_length=100, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    telefono = models.CharField(max_length=50, blank=False, null=False)
    direccion = models.CharField(max_length=400, blank=False, null=False)
    fecha_nacimiento = models.DateField(null=True, default=None, blank=True)

    class Meta:
        unique_together = ('nombres', 'apellidos')

    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.nombres


class Especialista(models.Model):

    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    especialidad = models.CharField(max_length=500, blank=False, null=False)
    activo = models.BooleanField(default=True, blank=False, null=False)

    def __unicode__(self):
        return self.especialidad

    def __str__(self):
        return self.especialidad


class Evento(models.Model):

    nombre = models.CharField(max_length=200, blank=False, null=False)
    fecha = models.DateTimeField(null=True, default=None, blank=True)
    lugar = models.CharField(max_length=400, blank=False, null=False)


    class Meta:
        unique_together = ('nombre', 'fecha', 'lugar')

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre


class Voluntario(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    fecha_visita = models.DateTimeField(null=True, default=None, blank=True)
    activo = models.BooleanField(default=True, blank=False, null=False)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return self.evento

    def __str__(self):
        return self.evento


class Benefactor(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    encargado = models.CharField(max_length=500, blank=False, null=False)
    activo = models.BooleanField(default=True, blank=False, null=False)

    def __unicode__(self):
        return self.encargado

    def __str__(self):
        return self.encargado


class Practicante(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    programa = models.CharField(max_length=500, blank=False, null=False)
    activo = models.BooleanField(default=True, blank=False, null=False)

    def __unicode__(self):
        return self.programa

    def __str__(self):
        return self.programa


class Asistencia(models.Model):
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=False, null=False)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    asistio = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        unique_together = ('id_evento', 'id_persona')

    def __unicode__(self):
        return self.id_persona

    def __str__(self):
        return '{0}'.format(self.id_persona)