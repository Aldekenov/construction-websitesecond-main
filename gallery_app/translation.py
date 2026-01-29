from modeltranslation.translator import register, TranslationOptions
from .models import GalleryCategory, GalleryImage

@register(GalleryCategory)
class GalleryCategoryTR(TranslationOptions):
    fields = ("title",)

@register(GalleryImage)
class GalleryImageTR(TranslationOptions):
    fields = ("project_name",)
