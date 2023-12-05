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

# # models.py
# from django.db import models

# class Recipe(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='recipe_images/')  # Aquí es donde se especifica la carpeta para almacenar las imágenes
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     # Otros campos que puedas necesitar

        

