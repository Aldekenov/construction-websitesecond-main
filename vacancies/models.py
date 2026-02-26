from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Vacancy(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название вакансии")
    slug = models.SlugField(max_length=220, unique=True, verbose_name="Slug")
    location = models.CharField(max_length=200, blank=True, verbose_name="Город/Локация")
    employment = models.CharField(max_length=120, blank=True, verbose_name="Тип занятости")
    description = RichTextUploadingField(verbose_name="Описание", blank=True)
    requirements = RichTextUploadingField(verbose_name="Требования", blank=True)
    conditions = RichTextUploadingField(verbose_name="Условия", blank=True)

    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Создано")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("vacancies:detail", kwargs={"slug": self.slug})


def resume_upload_to(instance, filename: str) -> str:
    # media/resumes/<vacancy_slug>/<timestamp>_<filename>
    ts = timezone.now().strftime("%Y%m%d_%H%M%S")
    return f"resumes/{instance.vacancy.slug}/{ts}_{filename}"


class VacancyApplication(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications", verbose_name="Вакансия")

    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    cover_letter = models.TextField(blank=True, verbose_name="Сопроводительное письмо")

    resume = models.FileField(upload_to=resume_upload_to, verbose_name="Резюме (файл)")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Создано")

    is_processed = models.BooleanField(default=False, verbose_name="Обработано")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Отклик на вакансию"
        verbose_name_plural = "Отклики на вакансии"

    def __str__(self):
        return f"{self.full_name} → {self.vacancy.title}"