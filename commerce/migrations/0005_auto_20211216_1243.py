# Generated by Django 3.2.9 on 2021-12-16 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_remove_product_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='product/', verbose_name='image'),
            preserve_default=False,
        ),
    ]