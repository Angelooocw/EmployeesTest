# Generated by Django 3.0.8 on 2020-07-31 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_auto_20200730_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='nombre completo'),
        ),
    ]