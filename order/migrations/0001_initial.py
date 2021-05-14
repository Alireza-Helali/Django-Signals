# Generated by Django 3.1.4 on 2020-12-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('total', models.PositiveIntegerField(blank=True)),
                ('total_price', models.PositiveIntegerField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('cars', models.ManyToManyField(to='cars.Car')),
            ],
        ),
    ]
