from csv import writer
from operator import mod
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('d', ' بایگانی ها '),
    ('p', 'منتشر شده'),
    ('w', 'پیش نویس'),
]


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name="تیتر")
    text = models.TextField(verbose_name="متن")
    image = models.ImageField(
        upload_to='images//%Y/%m/%d/', verbose_name="تصویر")
    data_added = models.DateTimeField(auto_now=True, verbose_name="تاریخ")
    writer = models.CharField(max_length=150, verbose_name="نویسنده")
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name="دسته بندی")
    source = models.ForeignKey(
        'Source', on_delete=models.DO_NOTHING, verbose_name="منبع")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت انتشار")

    class Meta:
        verbose_name = "اخبار"
        verbose_name_plural = "اخبار"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("News_detail", kwargs={"pk": self.pk})


# category


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


# source of news

class Source(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()

    class Meta:
        verbose_name = "منابع"
        verbose_name_plural = "منابع"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Source_detail", kwargs={"pk": self.pk})
