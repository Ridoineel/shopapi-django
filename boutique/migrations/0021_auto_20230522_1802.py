# Generated by Django 3.2.5 on 2023-05-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0020_auto_20230522_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.CharField(choices=[('annulee', 'Annulee'), ('en_preparation', 'En Preparation'), ('en_cours', 'En Cours'), ('terminee', 'Terminee')], default='en_preparation', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('en_attente', 'Attente'), ('en_livraison', 'Livraison'), ('annuler', 'Annuler')], default='en_attente', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('XOF', 'F Cfa'), ('EUR', 'Euro')], default='XOF', max_length=10),
        ),
    ]
