# Generated by Django 2.1 on 2018-08-15 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20180813_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='dni_referido',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='usuario.Usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cuenta_usuario',
            name='saldo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
