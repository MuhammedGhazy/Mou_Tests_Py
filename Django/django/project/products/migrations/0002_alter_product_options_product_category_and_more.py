# Generated by Django 5.0.6 on 2024-07-07 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-price']},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('phone', 'phone'), ('computer', 'computer')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(blank=True, default='content', null=True, verbose_name='Discription'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='phptps/24/07/images.jpeg', upload_to='photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, default=1000, max_digits=10),
        ),
    ]