from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(verbose_name='email')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и Время')
    
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Катогория')
    images = models.ImageField(upload_to='core', verbose_name='Изображения')
    def __str__(self):
        return self.title

class FoodCard(models.Model):
    name = models.CharField(max_length=50, verbose_name='Называния продукт' )
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='core', verbose_name='Изображения')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name