# Generated by Django 5.0.6 on 2024-05-22 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footwears',
            name='image',
            field=models.ImageField(default='', upload_to='footwers/'),
        ),
        migrations.CreateModel(
            name='DetailInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('footwears', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.footwears')),
            ],
            options={
                'db_table': 'detail_info',
            },
        ),
    ]
