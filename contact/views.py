from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import ContactForm, ContactInfo
from .forms import ContactFormForm


def contact(request):
    """Contact page with form"""
    form = ContactFormForm()
    contact_info = ContactInfo.objects.first()
    
    context = {
        'form': form,
        'contact_info': contact_info,
    }
    return render(request, 'contact/contact.html', context)


@require_http_methods(["POST"])
def contact_submit(request):
    """Handle contact form submission via HTMX"""
    form = ContactFormForm(request.POST)
    
    if form.is_valid():
        contact_form = form.save()
        
        # Return success response for HTMX
        if request.headers.get('HX-Request'):
            return render(request, 'contact/partials/contact_success.html', {
                'message': 'Спасибо за обратную связь! Мы ответим Вам в ближайшее время.'
            })
        else:
            messages.success(request, 'Спасибо за обратную связь! Мы ответим Вам в ближайшее время.')
            return redirect('contact:contact')
    else:
        # Return form with errors for HTMX
        if request.headers.get('HX-Request'):
            return render(request, 'contact/partials/contact_form.html', {
                'form': form
            })
        else:
            contact_info = ContactInfo.objects.first()
            return render(request, 'contact/contact.html', {
                'form': form,
                'contact_info': contact_info,
            })
