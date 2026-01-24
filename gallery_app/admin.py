from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'created_at')
    list_filter = ('category',)

    # change_list_template = "admin/gallery_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-multiple/', self.upload_multiple),
        ]
        return custom_urls + urls

    def upload_multiple(self, request):
        if request.method == "POST":
            category = request.POST.get("category")
            files = request.FILES.getlist("images")

            for f in files:
                GalleryImage.objects.create(
                    image=f,
                    category=category
                )

            self.message_user(request, "Фотографии успешно загружены")
            return redirect("..")

        return render(request, "admin/multi_upload.html", {
            "categories": GalleryImage.CATEGORY_CHOICES
        })
