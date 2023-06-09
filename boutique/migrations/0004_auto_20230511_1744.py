# Generated by Django 3.2.5 on 2023-05-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0003_product_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/product/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('XOF', 'F Cfa'), ('EUR', 'Euro')], default='XOF', max_length=10),
        ),
    ]
