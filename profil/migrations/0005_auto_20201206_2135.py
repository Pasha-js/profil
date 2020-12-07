# Generated by Django 3.1.3 on 2020-12-06 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0004_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profession',
            name='company_name_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Назва компанії'),
        ),
        migrations.AddField(
            model_name='profession',
            name='company_name_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Назва компанії'),
        ),
        migrations.AddField(
            model_name='profession',
            name='company_name_uk',
            field=models.CharField(max_length=30, null=True, verbose_name='Назва компанії'),
        ),
        migrations.AddField(
            model_name='profession',
            name='end_en',
            field=models.DateField(blank=True, null=True, verbose_name='Дата завершення'),
        ),
        migrations.AddField(
            model_name='profession',
            name='end_ru',
            field=models.DateField(blank=True, null=True, verbose_name='Дата завершення'),
        ),
        migrations.AddField(
            model_name='profession',
            name='end_uk',
            field=models.DateField(blank=True, null=True, verbose_name='Дата завершення'),
        ),
        migrations.AddField(
            model_name='profession',
            name='start_en',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='profession',
            name='start_ru',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='profession',
            name='start_uk',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='profession',
            name='title_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='profession',
            name='title_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='profession',
            name='title_uk',
            field=models.CharField(max_length=30, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='professioninfo',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='professioninfo',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='professioninfo',
            name='title_uk',
            field=models.CharField(max_length=100, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='softskill',
            name='descr_en',
            field=models.CharField(max_length=10, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='softskill',
            name='descr_ru',
            field=models.CharField(max_length=10, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='softskill',
            name='descr_uk',
            field=models.CharField(max_length=10, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='techskill',
            name='descr_en',
            field=models.CharField(max_length=15, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='techskill',
            name='descr_ru',
            field=models.CharField(max_length=15, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='techskill',
            name='descr_uk',
            field=models.CharField(max_length=15, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='descr_en',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='descr_ru',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='descr_uk',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Імя'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Імя'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='name_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='Імя'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='vacancy_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Посада'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='vacancy_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Посада'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='vacancy_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='Посада'),
        ),
        migrations.AlterField(
            model_name='techskill',
            name='descr',
            field=models.CharField(max_length=15, verbose_name='Опис'),
        ),
    ]