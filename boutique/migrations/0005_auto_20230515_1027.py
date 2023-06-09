# Generated by Django 3.2.5 on 2023-05-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0004_auto_20230511_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('XOF', 'F Cfa'), ('EUR', 'Euro')], default='XOF', max_length=10),
        ),
    ]
