from django.test import TestCase

import pytest
from django.core.exceptions import ValidationError
from api.models import Registro

@pytest.mark.django_db
def test_registro_model():
    # Crear una instancia de Registro
    registro = Registro(
        idRegistro=1,
        name='Nombre',
        apellido='Apellido',
        correo='correo@example.com',
        password='contraseña',
        confirmpassword='contraseña'
    )

    # Guardar en la base de datos
    registro.save()

    # Obtener la instancia guardada
    registro_db = Registro.objects.get(idRegistro=1)

    # Comprobar que los campos son iguales
    assert registro_db.idRegistro == 1
    assert registro_db.name == 'Nombre'
    assert registro_db.apellido == 'Apellido'
    assert registro_db.correo == 'correo@example.com'
    assert registro_db.password == 'contraseña'
    assert registro_db.confirmpassword == 'contraseña'

    # Modificar un campo y guardar de nuevo
    registro_db.name = 'Nuevo Nombre'
    registro_db.save()

    # Obtener la instancia actualizada
    registro_actualizado = Registro.objects.get(idRegistro=1)

    # Comprobar que el campo fue actualizado
    assert registro_actualizado.name == 'Nuevo Nombre'

    # Intentar crear una instancia con un campo no válido (correo inválido)
    with pytest.raises(ValidationError):
        Registro.objects.create(
            idRegistro=2,
            name='Nombre2',
            apellido='Apellido2',
            correo='correo_invalido',  # Esto debería generar una excepción de validación
            password='contraseña2',
            confirmpassword='contraseña2'
        )
