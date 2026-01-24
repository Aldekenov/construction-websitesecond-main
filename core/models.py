from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class CompanyInfo(models.Model):
    """Main company information"""
    company_name = models.CharField(max_length=200, default="Наименование компании", verbose_name="Компания")
    tagline = models.CharField(max_length=300, default="Слоган", verbose_name="Слоган")
    about_us = RichTextUploadingField(verbose_name="О нас")
    mission_statement = models.TextField(verbose_name="Миссия")
    years_experience = models.PositiveIntegerField(default=10, verbose_name="Опыт работы")
    projects_completed = models.PositiveIntegerField(default=100, verbose_name="Проекты")
    happy_clients = models.PositiveIntegerField(default=50, verbose_name="Клиенты")
    logo = models.ImageField(upload_to='company/', blank=True, null=True, verbose_name="Логотип")
    hero_image = models.ImageField(upload_to='company/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "информацию о компании"
        verbose_name_plural = "Информация о компании"

    def __str__(self):
        return self.company_name


class Service(models.Model):
    """Services offered by the company"""
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class", verbose_name="Иконка")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="Изображение")
    active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "услуги"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    """Client testimonials"""
    client_name = models.CharField(max_length=100, verbose_name="Заказчик")
    client_position = models.CharField(max_length=100, blank=True, verbose_name="Должность")
    client_company = models.CharField(max_length=100, blank=True, verbose_name="Компания")
    testimonial = models.TextField(verbose_name="Отзыв")
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 6)], verbose_name="Рейтинг")
    client_image = models.ImageField(upload_to='testimonials/', blank=True, null=True, verbose_name="Логотип")
    featured = models.BooleanField(default=False, verbose_name="На главную")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    image = models.ImageField(upload_to="about/reviews/", verbose_name="Изображение")

    class Meta:
        ordering = ['-featured', '-created_at']
        verbose_name_plural = "Отзывы"
        verbose_name = "отзывы"

    def __str__(self):
        return f"{self.client_name}, Оценка {self.rating}"


class ProjectGallery(models.Model):
    """Gallery of completed projects"""
    title = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='gallery/', verbose_name="Изображение")
    category = models.CharField(max_length=100, blank=True, verbose_name="Категория")
    completion_date = models.DateField(blank=True, null=True, verbose_name="Дата завершения")
    featured = models.BooleanField(default=False, verbose_name="На главную")
    order = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    class Meta:
        ordering = ['order', '-completion_date']
        verbose_name_plural = "Проекты"
        verbose_name = "проекты"

    def __str__(self):
        return self.title


class AboutGoals(models.Model):
    title = models.CharField(max_length=255, default="Цели")
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Цели"

    def __str__(self):
        return self.title


class AboutTasks(models.Model):
    title = models.CharField(max_length=255, default="Задачи")
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title


class AboutStrategy(models.Model):
    title = models.CharField(max_length=255, default="Стратегия")
    text = models.TextField()
    image = models.ImageField(upload_to="about/strategy/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Стратегия"

    def __str__(self):
        return self.title


class AboutLicense(models.Model):
    image = models.ImageField(upload_to="about/licenses/")
    description = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Лицензии"

    def __str__(self):
        return self.description or "Лицензия"


class AboutCertificate(models.Model):
    image = models.ImageField(upload_to="about/certificates/")
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.description or "Сертификат"


class AboutAward(models.Model):
    image = models.ImageField(upload_to="about/awards/")
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Награды"

    def __str__(self):
        return self.description or "Награда"
