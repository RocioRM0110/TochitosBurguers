from django.db import models


# Create your models here.
class Registro(models.Model):
    idRegistro = models.IntegerField(primary_key=True, db_column='idRegistro')
    name = models.CharField(max_length=100, db_column='name')
    apellido = models.CharField(max_length=100, db_column='apellido')
    correo = models.EmailField(db_column='correo')
    password = models.CharField(max_length=100, db_column='password')
    confirmpassword = models.CharField(max_length=100, db_column='confirmpassword')
    class Meta:
        db_table='Usuarios'
