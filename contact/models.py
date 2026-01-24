from django.db import models
from django.utils import timezone


class ContactForm(models.Model):
    CONTACT_TYPES = [
        ('general', 'Общий запрос'),
        ('quote', 'Запросить цену'),
        ('consultation', 'Консультация'),
        ('support', 'Поддержка'),
    ]

    name = models.CharField(max_length=100, verbose_name="Компания")
    email = models.EmailField(verbose_name="Почта")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPES, default='general', verbose_name="Вид обращения")
    subject = models.CharField(max_length=200, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Создано")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    responded = models.BooleanField(default=False, verbose_name="Отвечено")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Форма обратной связи"

    def __str__(self):
        return f"{self.name} - {self.subject}"


class ContactInfo(models.Model):
    """Company contact information"""
    company_name = models.CharField(max_length=200, default="Компания", verbose_name="Компания")
    address = models.TextField(verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")
    business_hours = models.TextField(default="Пн-Пт: 8:00-18:00, обед 12:00-14:00", verbose_name="Рабочие часы")
    emergency_phone = models.CharField(max_length=20, blank=True, verbose_name="Экстренные контакты")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.company_name
