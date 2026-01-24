from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import CompanyInfo, Service, Testimonial, ProjectGallery, AboutGoals, AboutTasks, AboutStrategy, AboutLicense, AboutCertificate, AboutAward
from blog.models import BlogPost
from contact.models import ContactForm


def home(request):
    """Homepage view with hero section and featured content"""
    context = {
        'company_info': CompanyInfo.objects.first(),
        'featured_services': Service.objects.filter(active=True)[:6],
        'featured_testimonials': Testimonial.objects.filter(featured=True)[:3],
        'featured_projects': ProjectGallery.objects.filter(featured=True)[:6],
        'latest_blog_posts': BlogPost.objects.filter(published=True)[:3],
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page with company information"""
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
    """Services page"""
    context = {
        'services': Service.objects.filter(active=True),
    }
    return render(request, 'core/services.html', context)


def gallery(request):
    """Project gallery page"""
    context = {
        'projects': ProjectGallery.objects.all(),
    }
    return render(request, 'core/gallery.html', context)


def gallery_detail(request, pk):
    """Detail view for a single gallery item"""
    gallery = get_object_or_404(ProjectGallery, pk=pk)
    company_info = CompanyInfo.objects.first()
    return render(request, 'core/gallery_detail.html', {'gallery': gallery, 'company_info': company_info})