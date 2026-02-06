from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    CompanyInfo, CEOProfile, Service, Testimonial, ProjectGallery,
    AboutGoals, AboutTasks, AboutStrategy, AboutLicense, AboutCertificate, AboutAward
)

# --- CORE ---

@admin.register(CompanyInfo)
class CompanyInfoAdmin(TranslationAdmin):
    # Обычно CompanyInfo одна запись -> фильтры не нужны.
    search_fields = ("company_name", "tagline")


@admin.register(CEOProfile)
class CEOProfileAdmin(TranslationAdmin):
    search_fields = ("full_name", "position", "education", "qualification", "experience_text")


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    search_fields = ("name",)
    list_filter = ("show_on_home",)
    # если есть поля типа is_active/sort/order — добавим list_filter
    # list_filter = ("is_active",)


@admin.register(Testimonial)
class TestimonialAdmin(TranslationAdmin):
    list_display = ("client_name", "client_company", "rating", "featured", "order", "created_at")
    list_filter = ("featured", "rating")
    list_editable = ("featured", "order")
    search_fields = ("client_name", "client_company", "client_position", "testimonial")
    ordering = ("-featured", "order", "-created_at")
    # если есть рейтинг/публикация/дата — добавим list_filter
    # list_filter = ("is_published",)


@admin.register(ProjectGallery)
class ProjectGalleryAdmin(TranslationAdmin):
    search_fields = ("title", "category")
    # если category — это choices/строка, list_filter тоже можно:
    list_filter = ("category",)


# --- ABOUT BLOCKS ---

@admin.register(AboutGoals)
class AboutGoalsAdmin(TranslationAdmin):
    search_fields = ("title", "text")


@admin.register(AboutTasks)
class AboutTasksAdmin(TranslationAdmin):
    search_fields = ("title", "text")


@admin.register(AboutStrategy)
class AboutStrategyAdmin(TranslationAdmin):
    search_fields = ("title", "text")


@admin.register(AboutLicense)
class AboutLicenseAdmin(TranslationAdmin):
    search_fields = ("description", "category")
    list_filter = ("category",)


@admin.register(AboutCertificate)
class AboutCertificateAdmin(TranslationAdmin):
    search_fields = ("description",)


@admin.register(AboutAward)
class AboutAwardAdmin(TranslationAdmin):
    search_fields = ("description",)
