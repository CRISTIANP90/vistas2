# Generated by Django 5.1.2 on 2024-10-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=60)),
                ('Autor', models.CharField(max_length=60)),
                ('Año_Publicacion', models.CharField(max_length=60)),
                ('Editorial', models.CharField(max_length=60)),
            ],
        ),
    ]
