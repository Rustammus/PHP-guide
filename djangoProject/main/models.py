import os

from django.db import models
from django.dispatch import receiver
# Create your models here.


class DataMain(models.Model):
    html_top = models.FileField(upload_to="file/main/", null=True, blank=True, default=None)
    pic_center = models.ImageField(upload_to="pictures/main/", null=True, blank=True, default=None)
    html_bot = models.FileField(upload_to="file/main/", null=True, blank=True, default=None)

    class Meta:
        verbose_name = "DB Главная"
        verbose_name_plural = "Главная страница"


class DataDemand(models.Model):
    html_top = models.FileField(name="Верхний HTML", upload_to="file/demand/", null=True)
    pic_center = models.ImageField(name="Картинка", upload_to="pictures/demand/", null=True)
    html_bot = models.FileField(name="Нижний HTML", upload_to="file/demand/", null=True)

    class Meta:
        verbose_name = "DB Востребованность"
        verbose_name_plural = "Страница Востребованность"


class DataGeo(models.Model):
    html_top = models.FileField(name="Верхний HTML", upload_to="file/geo/", null=True)
    pic_center = models.ImageField(name="Картинка", upload_to="pictures/geo/", null=True)
    html_bot = models.FileField(name="Нижний HTML", upload_to="file/geo/", null=True)

    class Meta:
        verbose_name = "DB География"
        verbose_name_plural = "Страница География"


class DataSkills(models.Model):
    html_top = models.FileField(name="Верхний HTML", upload_to="file/skills/", null=True)
    pic_center = models.ImageField(name="Картинка", upload_to="pictures/skills/", null=True)
    html_bot = models.FileField(name="Нижний HTML", upload_to="file/skills/", null=True)

    class Meta:
        verbose_name = "DB Навыки"
        verbose_name_plural = "Страница Навыки"


class DataRecVac(models.Model):
    text = models.TextField('Текст')

    class Meta:
        verbose_name = "DB Вакансии"
        verbose_name_plural = "Страница Вакансии"


