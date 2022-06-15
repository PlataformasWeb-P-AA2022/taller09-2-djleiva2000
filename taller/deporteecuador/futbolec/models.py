from django.db import models

# Create your models here.

class Equipo(models.Model):
    """
    """

    nombre = models.CharField("Nombre del equipo", max_length=30)
    siglas = models.CharField(max_length=30)
    username_t = models.CharField("Usuario de twitter",max_length=30, unique=True)
    


    def __str__(self):
        return "%s - %s - %s " % (
                self.nombre, 
                self.siglas,
                self.username_t)


class Jugador(models.Model):
    """
    """
    nombrej = models.CharField("Nombre ", max_length=30)
    posicion = models.CharField(max_length=30)
    numero_c = models.IntegerField("Numero de camiseta")
    sueldo = models.IntegerField("sueldo")
    equipo = models.ForeignKey(Equipo,related_name= "los jugadores ",
            on_delete= models.CASCADE )


    def __str__(self):
        return " %s - %s - %d - %d - %s "  % (self.nombrej,
        self.posicion,
        self.numero_c,
        self.sueldo,
        self.equipo)


class Campeonato(models.Model):
    """
    """
    nombre_campionato = models.CharField( max_length=30)
    nombre_auspiciante = models.CharField(max_length=30)



    def __str__(self):
        return "%s - %s  " % (
                self.nombre_campionato, 
                self.nombre_auspiciante)

class Campeonatoequipo (models.Model):
    """
    """
    anio = models.IntegerField("Año ")
    equipo = models.ForeignKey(Equipo, related_name = "campeonato equipo",
         on_delete =models.CASCADE)

    campeonato = models.ForeignKey(Campeonato, related_name = "campeonato ",
         on_delete =models.CASCADE)

    def __str__(self):
        return " %d - %s - %s "  % (
            self.anio,
            self.equipo,
            self.campeonato)