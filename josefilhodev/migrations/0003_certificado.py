# Generated by Django 4.2.4 on 2023-08-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josefilhodev', '0002_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificado_name', models.CharField(max_length=100)),
                ('certificado_link', models.URLField()),
                ('instituicao_img', models.URLField()),
            ],
        ),
    ]
