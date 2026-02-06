from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import CompanyInfo, Service, Testimonial, ProjectGallery, AboutGoals, AboutTasks, AboutStrategy, AboutLicense, AboutCertificate, AboutAward, CEOProfile
from blog.models import BlogPost
from contact.models import ContactForm
from django.db.models.functions import ExtractYear


def home(request):
    """Домашняя страница"""
    context = {
        'company_info': CompanyInfo.objects.first(),
        'ceo': CEOProfile.objects.filter(is_active=True).first(),
        'featured_services': Service.objects.filter(show_on_home=True)[:6],
        'featured_testimonials': Testimonial.objects.filter(featured=True).order_by('order', '-created_at'),
        'featured_projects': ProjectGallery.objects.filter(featured=True)[:6],
        'latest_blog_posts': BlogPost.objects.filter(published=True)[:3],
    }
    return render(request, 'core/home.html', context)


def about(request):
    """Страница: О нас"""
    goals = AboutGoals.objects.all()
    tasks = AboutTasks.objects.all()

    for g in goals:
        g.lines = [line.strip() for line in g.text.split("\n") if line.strip()]

    for t in tasks:
        t.lines = [line.strip() for line in t.text.split("\n") if line.strip()]

    context = {
        'company_info': CompanyInfo.objects.first(),
        'testimonials': Testimonial.objects.all()[:6],
        "goals": goals,
        "tasks": tasks,
        "strategy": AboutStrategy.objects.all(),
        "licenses": AboutLicense.objects.all(),
        "certificates": AboutCertificate.objects.all(),
        "awards": AboutAward.objects.all(),
    }
    return render(request, 'core/about.html', context)


def services(request):
    """Страница: Деятельность"""
    context = {
        'services': Service.objects.filter(active=True),
    }
    return render(request, 'core/services.html', context)


def gallery(request):
    """Страница: Проекты"""
    category = (request.GET.get("category") or "").strip()
    year = (request.GET.get("year") or "").strip()

    qs = ProjectGallery.objects.all()

    if category:
        qs = qs.filter(category=category)

    if year:
        try:
            qs = qs.filter(completion_date__year=int(year))
        except ValueError:
            pass

    categories = (ProjectGallery.objects
                  .exclude(category__isnull=True)
                  .exclude(category__exact="")
                  .values_list("category", flat=True)
                  .distinct()
                  .order_by("category"))

    years = (ProjectGallery.objects
             .exclude(completion_date__isnull=True)
             .annotate(y=ExtractYear("completion_date"))
             .values_list("y", flat=True)
             .distinct()
             .order_by("-y"))

    context = {
        "projects": qs,
        "categories": categories,
        "years": years,
        "selected_category": category,
        "selected_year": year,
    }
    return render(request, "core/gallery.html", context)


def gallery_detail(request, pk):
    """Страница: Проекты подробно"""
    gallery = get_object_or_404(ProjectGallery, pk=pk)
    company_info = CompanyInfo.objects.first()
    return render(request, 'core/gallery_detail.html', {'gallery': gallery, 'company_info': company_info})