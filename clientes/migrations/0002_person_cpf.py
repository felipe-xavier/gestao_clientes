# Generated by Django 2.2.6 on 2019-10-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cpf',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
