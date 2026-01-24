from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost, BlogCategory


def blog_list(request):
    """Blog listing page with pagination"""
    posts = BlogPost.objects.filter(published=True)
    
    # Pagination
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'categories': BlogCategory.objects.all(),
        'featured_posts': BlogPost.objects.filter(published=True, featured=True)[:3],
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Individual blog post detail"""
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    related_posts = BlogPost.objects.filter(
        published=True
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/blog_detail.html', context)


def blog_category(request, category_slug):
    """Blog posts filtered by category"""
    category = get_object_or_404(BlogCategory, slug=category_slug)
    posts = BlogPost.objects.filter(
        blogpostcategory__category=category,
        published=True
    )
    
    # Pagination
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'posts': page_obj,
        'category': category,
        'categories': BlogCategory.objects.all(),
    }
    return render(request, 'blog/blog_category.html', context)
