# Generated by Django 3.2.5 on 2023-05-19 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boutique', '0013_auto_20230517_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderedproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='boutique.order'),
        ),
        migrations.AlterField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('XOF', 'F Cfa'), ('EUR', 'Euro')], default='XOF', max_length=10),
        ),
    ]