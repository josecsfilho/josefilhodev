# Generated by Django 4.2.4 on 2023-08-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josefilhodev', '0003_certificado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('instituicao', models.CharField(max_length=200)),
                ('periodo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=200)),
                ('empresa', models.CharField(max_length=200)),
                ('periodo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
