from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import GalleryCategory, GalleryImage

PER_PAGE = 14


def gallery(request):
    """Страница: Фотогалерея"""
    year = request.GET.get("year")
    project = request.GET.get("project")

    years = (GalleryImage.objects
             .exclude(project_year__isnull=True)
             .values_list("project_year", flat=True)
             .distinct()
             .order_by("-project_year"))

    projects_qs = GalleryImage.objects.exclude(project__isnull=True).select_related("project")
    if year:
        projects_qs = projects_qs.filter(project_year=year)

    projects = (projects_qs
                .values("project_id", "project__title")
                .distinct()
                .order_by("project__title"))

    categories = GalleryCategory.objects.all().order_by("title")

    categories_data = []
    for cat in categories:
        qs = cat.images.all().select_related("project").order_by("-created_at")

        if year:
            qs = qs.filter(project_year=year)
        if project:
            qs = qs.filter(project_id=project)

        page_param = f"page_{cat.slug}"
        page_number = request.GET.get(page_param)
        paginator = Paginator(qs, PER_PAGE)
        page_obj = paginator.get_page(page_number)

        categories_data.append({
            "category": cat,
            "page_obj": page_obj,
            "page_param": page_param,
        })

    return render(request, "gallery_app/gallery.html", {
        "categories_data": categories_data,
        "years": years,
        "projects": projects,
        "selected_year": str(year) if year else "",
        "selected_project": str(project) if project else "",
    })