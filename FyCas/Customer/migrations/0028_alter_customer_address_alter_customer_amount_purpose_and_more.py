# Generated by Django 5.0 on 2024-04-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0027_alter_customer_moneda_alter_customer_ocupacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='amount_purpose',
            field=models.TextField(blank=True, max_length=355),
        ),
        migrations.AlterField(
            model_name='customer',
            name='atraso121_150',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='atraso151_180',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='atraso181_o_mas',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='atraso1_30',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='atraso31_60',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='atraso61_90',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='atraso91_120',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='balance_corte',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='calle_numero',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='calle_numero_trabajo',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cantidad_cuota',
            field=models.CharField(blank=True, default='6', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cargo',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ciudad',
            field=models.CharField(blank=True, default='Santo Domingo Este', max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ciudad_trabaja',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='code_customer',
            field=models.CharField(blank=True, default='', max_length=122000),
        ),
        migrations.AlterField(
            model_name='customer',
            name='credito_aprovado',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='dir_referencia',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='dir_referencia_trabajo',
            field=models.CharField(blank=True, default='', max_length=244),
        ),
        migrations.AlterField(
            model_name='customer',
            name='direccion',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='direccion_trabajo',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='dni',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='empresa_trabaja',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='estado_civil',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='customer',
            name='estatus',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fecha_apertura',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fecha_ultimo_pago',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fecha_vencimiento',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='forma_pago',
            field=models.CharField(blank=True, default='Mensual', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lat',
            field=models.CharField(blank=True, default='', max_length=100000000050005),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lon',
            field=models.CharField(blank=True, default='', max_length=100000000000000055),
        ),
        migrations.AlterField(
            model_name='customer',
            name='moneda',
            field=models.CharField(blank=True, default='RD$', max_length=3),
        ),
        migrations.AlterField(
            model_name='customer',
            name='moneda_prestamo',
            field=models.CharField(blank=True, default='RD$', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='monto_adeudado',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='monto_ultimo_pago',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='municipio',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='municipio_trabaja',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nacimiento',
            field=models.CharField(blank=True, default='10/11/2001', max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nacionalidad',
            field=models.CharField(blank=True, default='DOMINICANA', max_length=25),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name_r1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name_r2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='number_r1',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='number_r2',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='numeoro_cuenta',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ocupacion',
            field=models.CharField(blank=True, default='Estudiante', max_length=25),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pago_mandatorio_cuota',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pais',
            field=models.CharField(blank=True, default='REPUBLICA DOMINICANA', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pais_trabajo',
            field=models.CharField(blank=True, default='REPUBLICA DOMINICANA', max_length=244),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=18),
        ),
        migrations.AlterField(
            model_name='customer',
            name='provincia',
            field=models.CharField(blank=True, default='SANTO DOMINGO DE GUZMAN', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='provincia_trabajo',
            field=models.CharField(blank=True, default='SANTO DOMINGO DE GUZMAN', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='references_peopple',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='relacion_tipo',
            field=models.CharField(blank=True, default='1', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='salario_m',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sector',
            field=models.CharField(blank=True, default='', max_length=244),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sexo',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tasa_interes',
            field=models.CharField(blank=True, default='0.15', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tipo_prestamo',
            field=models.CharField(blank=True, default='N', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='total_atraso',
            field=models.CharField(blank=True, default='', max_length=233),
        ),
        migrations.AlterField(
            model_name='customer',
            name='type_input',
            field=models.CharField(blank=True, default='P', max_length=2),
        ),
        migrations.AlterField(
            model_name='customer',
            name='work_information',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]