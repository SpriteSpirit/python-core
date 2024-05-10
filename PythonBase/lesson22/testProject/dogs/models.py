from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Кличка')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='Фото', )
    birth_date = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} ({self.breed.name})'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'


