from django.db import models
#se crearon los modelos de las tablas donde se pueden ver en admin
#para esto es necesario hacer la conexion con postgres y la migracion
# Create your models here.
class Medico(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    especialidad= models.CharField(max_length=50)

    def __str__(self) :
         return f" Medico: {self.nombre}"

   

class Paciente(models.Model):
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     fecha_nacimiento = models.DateField()
     sexo = models.CharField(max_length=12)
     altura = models.FloatField()
     med = models.ForeignKey(Medico ,on_delete=models.CASCADE)

   

class Paciente2(models.Model):
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     fecha_nacimiento = models.DateField()
     sexo = models.CharField(max_length=12)
     altura = models.FloatField()
     med = models.ForeignKey(Medico ,on_delete=models.CASCADE)

   
 
     
   