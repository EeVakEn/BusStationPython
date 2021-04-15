# Generated by Django 3.2 on 2021-04-12 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210412_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='id_bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.bus'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='id_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.route'),
        ),
    ]