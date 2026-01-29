from modeltranslation.translator import register, TranslationOptions
from .models import ContactInfo

@register(ContactInfo)
class ContactInfoTR(TranslationOptions):
    fields = ("company_name", "address", "business_hours", "emergency_phone")
