from django.db import models

class TechSkill(models.Model):
    descr = models.CharField('Опис', max_length=15)

class SoftSkill(models.Model):
    descr = models.CharField('Опис', max_length=10)

class Profession(models.Model):
    title = models.CharField('Опис', max_length=30)
    company_name = models.CharField('Назва компанії', max_length=30)
    start = models.DateField('Дата')
    end = models.DateField('Дата завершення', blank=True, null=True)

class ProfessionInfo(models.Model):
    profession = models.ForeignKey(to=Profession, on_delete=models.CASCADE)
    title = models.CharField('Опис', max_length=100)

class UserInfo(models.Model):
    vacancy = models.CharField('Посада', max_length=50)
    name = models.CharField('Імя', max_length=50)
    descr = models.TextField('Опис')

