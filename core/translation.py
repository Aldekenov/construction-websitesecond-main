from modeltranslation.translator import translator, TranslationOptions
from .models import Service, AboutPage  # подставь свои модели

class ServiceTranslationOptions(TranslationOptions):
    fields = ("title", "description")

translator.register(Service, ServiceTranslationOptions)

class AboutPageTranslationOptions(TranslationOptions):
    fields = ("title", "content")

translator.register(AboutPage, AboutPageTranslationOptions)