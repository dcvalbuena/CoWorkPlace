# Generated by Django 3.2.7 on 2021-09-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0003_auto_20210918_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoLugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='pago_reserva_sala',
            name='IdLocacion',
        ),
        migrations.RemoveField(
            model_name='pago_reserva_sala',
            name='IdReserva',
        ),
        migrations.RemoveField(
            model_name='pago_reserva_sala',
            name='IdSala',
        ),
        migrations.RemoveField(
            model_name='puesto_cow',
            name='IdLocacion',
        ),
        migrations.RemoveField(
            model_name='reserva_puesto_cow',
            name='IdLocacion',
        ),
        migrations.RemoveField(
            model_name='reserva_puesto_cow',
            name='IdPuesto',
        ),
        migrations.RemoveField(
            model_name='reserva_sala_cow',
            name='IdLocacion',
        ),
        migrations.RemoveField(
            model_name='reserva_sala_cow',
            name='IdSala',
        ),
        migrations.RemoveField(
            model_name='sala_cow',
            name='IdLocacion',
        ),
        migrations.AlterField(
            model_name='locacion',
            name='Capacidad_Individual',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locacion',
            name='Capacidad_Salas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locacion',
            name='Valoracion_Clientes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Pago_Reserva_Puesto',
        ),
        migrations.DeleteModel(
            name='Pago_Reserva_Sala',
        ),
        migrations.DeleteModel(
            name='Puesto_COW',
        ),
        migrations.DeleteModel(
            name='Reserva_Puesto_COW',
        ),
        migrations.DeleteModel(
            name='Reserva_Sala_COW',
        ),
        migrations.DeleteModel(
            name='Sala_COW',
        ),
    ]
