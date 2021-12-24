# Generated by Django 3.2.9 on 2021-12-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_auto_20211216_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='title',
            field=models.CharField(choices=[('NEW', 'NEW'), ('PROCESSING', 'PROCESSING'), ('SHIPPED', 'SHIPPED'), ('COMPLETED', 'COMPLETED'), ('REFUNDED', 'REFUNDED')], default='NEW', max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=True, verbose_name='ordered'),
        ),
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]