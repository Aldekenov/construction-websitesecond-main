from django.core.paginator import Paginator
from .models import GalleryImage, GalleryCategory
from django.shortcuts import render


def gallery(request):
    categories = GalleryCategory.objects.all()

    workdays = GalleryImage.objects.filter(
        category="workdays"
    ).order_by("-created_at")

    paginator = Paginator(workdays, 24)
    page_number = request.GET.get("page")
    workdays_page = paginator.get_page(page_number)

    return render(request, "gallery_app/gallery.html", {
        "categories": categories,
        "workdays_page": workdays_page,
    })