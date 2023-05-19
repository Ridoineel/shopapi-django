# Generated by Django 3.2.5 on 2023-05-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0005_auto_20230515_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('XOF', 'F Cfa'), ('EUR', 'Euro')], default='XOF', max_length=10),
        ),
    ]
