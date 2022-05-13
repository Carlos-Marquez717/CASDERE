# Generated by Django 4.0.3 on 2022-05-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(max_length=12)),
                ('Email', models.EmailField(max_length=50)),
                ('Asunto', models.CharField(max_length=50)),
                ('Mensaje', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'nombre',
                'verbose_name_plural': 'nombres',
            },
        ),
    ]