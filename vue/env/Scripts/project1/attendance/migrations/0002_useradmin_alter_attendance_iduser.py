# Generated by Django 4.1.7 on 2023-03-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='USERADMIN',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mame', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='iduser',
            field=models.IntegerField(unique=True),
        ),
    ]
