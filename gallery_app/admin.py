from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path
from django.utils.html import format_html

from .models import GalleryImage, GalleryCategory


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    change_list_template = "admin/gallery_app/galleryimage/change_list.html"
    list_display = ("id", "thumb", "category", "project_year", "project_name", "created_at")
    list_filter = ("category", "project_year", "created_at")
    search_fields = ("project_name", "category__title", "category__slug")
    list_editable = ("category", "project_year", "project_name")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    autocomplete_fields = ("category",)

    def thumb(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="70" height="70" style="object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )
        return "-"
    thumb.short_description = "Эскиз"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("upload-multiple/", self.admin_site.admin_view(self.upload_multiple), name="galleryimage_upload_multiple"),
        ]
        return custom_urls + urls

    def upload_multiple(self, request):
        if request.method == "POST":
            cat_id = request.POST.get("category")
            category = get_object_or_404(GalleryCategory, id=cat_id)

            project_year = request.POST.get("project_year")
            project_name = (request.POST.get("project_name") or "").strip()

            files = request.FILES.getlist("images")
            for f in files:
                GalleryImage.objects.create(
                    image=f,
                    category=category,
                    project_year=int(project_year) if project_year else None,
                    project_name=project_name,
                )

            self.message_user(request, "Фотографии успешно загружены")
            return redirect("..")

        return render(request, "admin/multi_upload.html", {
            "categories": GalleryCategory.objects.all().order_by("title"),
        })
