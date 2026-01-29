from modeltranslation.translator import register, TranslationOptions
from .models import (
    CompanyInfo, CEOProfile, Service, Testimonial, ProjectGallery,
    AboutGoals, AboutTasks, AboutStrategy, AboutLicense, AboutCertificate, AboutAward
)

@register(CompanyInfo)
class CompanyInfoTR(TranslationOptions):
    fields = ("company_name", "tagline", "about_us", "mission_statement")

@register(CEOProfile)
class CEOProfileTR(TranslationOptions):
    fields = ("full_name", "position", "quote", "education", "qualification", "experience_text", "key_skills")

@register(Service)
class ServiceTR(TranslationOptions):
    fields = ("name", "description")

@register(Testimonial)
class TestimonialTR(TranslationOptions):
    fields = ("client_name", "client_position", "client_company", "testimonial")

@register(ProjectGallery)
class ProjectGalleryTR(TranslationOptions):
    fields = ("title", "description", "category")

@register(AboutGoals)
class AboutGoalsTR(TranslationOptions):
    fields = ("title", "text")

@register(AboutTasks)
class AboutTasksTR(TranslationOptions):
    fields = ("title", "text")

@register(AboutStrategy)
class AboutStrategyTR(TranslationOptions):
    fields = ("title", "text")

@register(AboutLicense)
class AboutLicenseTR(TranslationOptions):
    fields = ("description", "category")

@register(AboutCertificate)
class AboutCertificateTR(TranslationOptions):
    fields = ("description",)

@register(AboutAward)
class AboutAwardTR(TranslationOptions):
    fields = ("description",)
