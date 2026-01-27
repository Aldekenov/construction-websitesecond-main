from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import GalleryCategory, GalleryImage

PER_PAGE = 24

def gallery(request):
    year = request.GET.get("year")      # например "2025"
    project = request.GET.get("project")  # например "KPO склад"

    # варианты для выпадающих списков — из БД
    years = (GalleryImage.objects
             .exclude(project_year__isnull=True)
             .values_list("project_year", flat=True)
             .distinct()
             .order_by("-project_year"))

    # проекты лучше подстраивать под выбранный год (если год выбран)
    projects_qs = GalleryImage.objects.exclude(project_name="")
    if year:
        projects_qs = projects_qs.filter(project_year=year)

    projects = (projects_qs
                .values_list("project_name", flat=True)
                .distinct()
                .order_by("project_name"))

    categories = GalleryCategory.objects.all().order_by("title")

    categories_data = []
    for cat in categories:
        qs = cat.images.all().order_by("-created_at")  # related_name="images" :contentReference[oaicite:3]{index=3}

        if year:
            qs = qs.filter(project_year=year)
        if project:
            qs = qs.filter(project_name=project)

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
        "selected_project": project or "",
    })