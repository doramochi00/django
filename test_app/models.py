from django.db import models

# Create your models here.
class book_list(models.Model):
    book_name = models.CharField(verbose_name='本の名前', max_length=200)
    author = models.CharField(verbose_name='作者', max_length=200)
    publisher = models.CharField(verbose_name='出版社', max_length=200)
    price = models.CharField(verbose_name='価格', max_length=200)