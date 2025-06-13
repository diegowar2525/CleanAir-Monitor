from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator 

validar_password = RegexValidator(
    regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,25}$",
    message="El formato de la contraseña es inválido. Debe tener entre 8 y 25 caracteres. Debe tener al menos una mayúscula, una minúscula, un número y un caracter especial"
)