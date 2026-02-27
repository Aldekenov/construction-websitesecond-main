from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Vacancy, VacancyApplication
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Vacancy)
class VacancyAdmin(TranslationAdmin):
    list_display = ["title", "is_active", "created_at"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["is_active", "created_at"]
    search_fields = ["title", "description", "requirements", "conditions"]

@admin.register(VacancyApplication)
class VacancyApplicationAdmin(admin.ModelAdmin):
    list_display = ["full_name", "vacancy", "email", "phone", "created_at", "is_processed", "resume_link", "export_link"]
    list_filter = ["vacancy", "is_processed", "created_at"]
    search_fields = ["full_name", "email", "phone", "cover_letter"]
    list_editable = ["is_processed"]
    readonly_fields = ["created_at"]

    def resume_link(self, obj):
        if not obj.resume:
            return "-"
        return format_html('<a href="{}" target="_blank">Файл</a>', obj.resume.url)

    resume_link.short_description = "Резюме"

    def export_link(self, obj):
        url = reverse("vacancies:export_xlsx")
        return format_html('<a class="button" href="{}">Excel</a>', url)

    export_link.short_description = "Выгрузка"