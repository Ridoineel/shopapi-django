# Generated by Django 3.2.5 on 2023-05-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0007_auto_20230515_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('XOF', 'F Cfa'), ('EUR', 'Euro')], default='XOF', max_length=10),
        ),
    ]
