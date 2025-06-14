# Generated by Django 5.2.3 on 2025-06-13 00:56

import apps.custom_auth.validators.email
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='El formato del nombre / apellido tiene un formato inválido. No debe tener números ni caracteres especiales (incluyendo el signo _)), su longitud debe estar entre los 3 y 30 caracteres', regex='^[A-Za-zÁÉÍÓÚáéíóúÑñ\\s]{3,30}$')])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='El formato del nombre / apellido tiene un formato inválido. No debe tener números ni caracteres especiales (incluyendo el signo _)), su longitud debe estar entre los 3 y 30 caracteres', regex='^[A-Za-zÁÉÍÓÚáéíóúÑñ\\s]{3,30}$')])),
                ('username', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='El formato del username es inválido. Debe tener entre 6 y 20 caracteres, no puede comenzar con un número, no puede tener caracteres especiales (excepto el _) ni espacios en blanco', regex='^(?![0-9])[a-zA-Z_][a-zA-Z0-9_]{5,19}$')])),
                ('email', models.EmailField(max_length=254, unique=True, validators=[apps.custom_auth.validators.email.validar_email])),
                ('password', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(message='El formato de la contraseña es inválido. Debe tener entre 8 y 25 caracteres. Debe tener al menos una mayúscula, una minúscula, un número y un caracter especial', regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[^a-zA-Z0-9]).{8,25}$')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
    ]
