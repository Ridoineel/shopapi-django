# Generated by Django 3.2.5 on 2023-05-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('XOF', 'F Cfa'), ('EUR', 'Euro')], default='XOF', max_length=10),
        ),
    ]
