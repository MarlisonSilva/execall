# Generated by Django 4.1.4 on 2022-12-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='categoria',
            field=models.CharField(choices=[('Peitoral', 'Peitoral'), ('Pernas', 'Pernas'), ('Costas', 'Costas'), ('Bíceps', 'Bíceps'), ('Tríceps', 'Tríceps')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
