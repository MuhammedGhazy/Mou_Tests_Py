# Generated by Django 5.1 on 2024-08-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Enter Item Name', max_length=30),
        ),
    ]
