from modeltranslation.translator import register, TranslationOptions
from .models import BlogPost, BlogCategory

@register(BlogPost)
class BlogPostTR(TranslationOptions):
    fields = ("title", "content", "excerpt")

@register(BlogCategory)
class BlogCategoryTR(TranslationOptions):
    fields = ("name", "description")
