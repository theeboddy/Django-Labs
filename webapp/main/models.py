from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    role = models.CharField("Роль пользователя", max_length=200, default="User")


class Company(models.Model):
    company_name = models.CharField("Название компании", max_length=200)

    def __str__(self):
        return f'{self.company_name}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Room(models.Model):
    room_name = models.CharField("Название комнаты", max_length=200)

    def __str__(self):
        return f'{self.room_name}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Section(models.Model):
    name = models.CharField("Название отдела", max_length=200)
    leader = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Movement(models.Model):
    date = models.DateField()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Перемещение'
        verbose_name_plural = 'Перемещения'