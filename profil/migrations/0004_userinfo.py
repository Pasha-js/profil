# Generated by Django 3.1.3 on 2020-12-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0003_profession_professioninfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy', models.CharField(max_length=50, verbose_name='Посада')),
                ('name', models.CharField(max_length=50, verbose_name='Імя')),
                ('descr', models.TextField(verbose_name='Опис')),
            ],
        ),
    ]
