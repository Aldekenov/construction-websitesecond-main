from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Vacancy, VacancyApplication

@admin.register(Vacancy)
class VacancyAdmin(TranslationAdmin):
    list_display = ["title", "is_active", "created_at"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["is_active", "created_at"]
    search_fields = ["title", "description", "requirements", "conditions"]

@admin.register(VacancyApplication)
class VacancyApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "vacancy", "email", "phone", "created_at", "is_processed")
    list_filter = ("vacancy", "is_processed", "created_at")
    search_fields = ("full_name", "email", "phone", "cover_letter")
    list_editable = ("is_processed",)
    readonly_fields = ("created_at",)