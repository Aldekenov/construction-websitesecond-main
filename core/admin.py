from django.contrib import admin
from django.utils.html import format_html
from .models import CompanyInfo, Service, Testimonial, ProjectGallery, AboutGoals, AboutTasks, AboutStrategy, AboutLicense, AboutCertificate, AboutAward, CEOProfile


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'years_experience', 'projects_completed', 'happy_clients']
    
    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CEOProfile)
class CEOProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "is_active")
    list_editable = ("is_active",)
    search_fields = ("full_name", "position")

    fieldsets = (
        ("Основное", {
            "fields": ("is_active", "full_name", "position", "photo", "quote")
        }),
        ("Профиль", {
            "fields": ("education", "qualification", "experience_years", "experience_text", "key_skills")
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'order', 'image_preview']
    list_filter = ['active']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']
    list_editable = ['active', 'order']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Эскиз"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_company', 'rating', 'featured', 'created_at']
    list_filter = ['rating', 'featured', 'created_at']
    search_fields = ['client_name', 'client_company', 'testimonial']
    ordering = ['-featured', '-created_at']
    list_editable = ['featured']


@admin.register(ProjectGallery)
class ProjectGalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'completion_date', 'featured', 'order', 'image_preview']
    list_filter = ['category', 'featured', 'completion_date']
    search_fields = ['title', 'description', 'category']
    ordering = ['order', '-completion_date']
    list_editable = ['featured', 'order']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', 
                             obj.image.url)
        return "No Image"
    image_preview.short_description = "Эскиз"


admin.site.register(AboutGoals)
admin.site.register(AboutTasks)
admin.site.register(AboutStrategy)
admin.site.register(AboutLicense)
admin.site.register(AboutCertificate)
admin.site.register(AboutAward)