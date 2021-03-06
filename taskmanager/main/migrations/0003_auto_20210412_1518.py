# Generated by Django 3.2 on 2021-04-12 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_bus_id_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_number', models.CharField(max_length=9, unique=True, verbose_name='Номер маршрута')),
                ('stop_from_address', models.CharField(max_length=50, verbose_name='Пункт отправки')),
                ('stop_to_address', models.CharField(max_length=500, verbose_name='Пункт назначения')),
            ],
        ),
        migrations.AlterField(
            model_name='bus',
            name='regist_number',
            field=models.CharField(max_length=9, unique=True, verbose_name='Регистрационный номер'),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_num', models.CharField(max_length=20, unique=True, verbose_name='Номер рейса')),
                ('driver', models.CharField(max_length=50, verbose_name='Имя водителя')),
                ('ticket_price', models.IntegerField()),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('id_bus', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.bus')),
                ('id_route', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.route')),
            ],
        ),
    ]
