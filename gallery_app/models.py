from django.db import models
from django import forms


# calendar_app/models.py
class GalleryCategory(models.Model):
    title = models.CharField("Название", max_length=150)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категория галереи"
        verbose_name_plural = "Категории галереи"

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/")
    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Категория"
    )
    project_name = models.CharField("Проект", max_length=200, blank=True, default="")
    project_year = models.PositiveSmallIntegerField("Год", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"

    def __str__(self):
        return f"{self.category.title}"
