from django.contrib import admin
from .models import ContactForm, ContactInfo


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact_type', 'subject', 'created_at', 'is_read', 'responded']
    list_filter = ['contact_type', 'is_read', 'responded', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_editable = ['is_read', 'responded']
    readonly_fields = ['created_at']

    def has_add_permission(self, request):
        # Prevent manual addition of contact forms through admin
        return False


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'phone', 'email']
    
    def has_add_permission(self, request):
        # Only allow one contact info instance
        return not ContactInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of contact info
        return False
