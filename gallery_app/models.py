from django.db import models
from django import forms
from core.models import ProjectGallery


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
    project = models.ForeignKey(
        ProjectGallery,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="gallery_images",
        verbose_name="Проект",
    )
    project_year = models.PositiveSmallIntegerField("Год", null=True, blank=True)
    project_name = models.CharField("Проект", max_length=200, blank=True, default="", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # если выбран проект — год тянем из completion_date
        if self.project and self.project.completion_date:
            self.project_year = self.project.completion_date.year

        # (опционально) держим project_name синхронизированным, чтобы старые места не падали
        if self.project:
            self.project_name = self.project.title

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"

    def __str__(self):
        return f"{self.category.title}"
