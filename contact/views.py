from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
import os

from .forms import ContactFormForm
from .models import ContactInfo


def contact(request):
    """
    Страница /contact/
    """
    form = ContactFormForm()
    contact_info = ContactInfo.objects.first()

    return render(
        request,
        "contact/contact.html",
        {
            "form": form,
            "contact_info": contact_info,
        }
    )


def contact_submit(request):
    """
    HTMX submit:
    - форма на странице контактов
    - форма в футере
    """
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed")

    form = ContactFormForm(request.POST)
    contact_info = ContactInfo.objects.first()

    if not form.is_valid():
        # Ошибки валидации — вернуть форму обратно
        return render(
            request,
            "contact/partials/contact_form.html",
            {
                "form": form,
                "contact_info": contact_info,
            }
        )

    # ===== СОХРАНЕНИЕ В БД =====
    obj = form.save()

    ctx = {
        "subject": obj.subject,
        "name": obj.name,
        "email": obj.email,
        "phone": obj.phone,
        "contact_type": obj.get_contact_type_display(),
        "message": obj.message,
        "created_at": timezone.localtime(obj.created_at).strftime("%d.%m.%Y %H:%M"),
        "site_domain": "tess-project.kz",
    }

    if obj.email:
        text_body = render_to_string("contact/emails/contact_client.txt", ctx)
        html_body = render_to_string("contact/emails/contact_client.html", ctx)

        msg = EmailMultiAlternatives(
            subject=f"Мы получили ваше обращение — {obj.subject}",
            body=text_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[obj.email],
        )
        msg.attach_alternative(html_body, "text/html")

        logo_path = os.path.join(settings.MEDIA_ROOT, "about", "logo.png")

        if os.path.exists(logo_path):
            with open(logo_path, "rb") as f:
                img = MIMEImage(f.read())
                img.add_header("Content-ID", "<tess_logo>")
                img.add_header("Content-Disposition", "inline", filename="logo.png")
                msg.attach(img)

        msg.send(fail_silently=False)


    text_body = render_to_string("contact/emails/contact_admin.txt", ctx)
    html_body = render_to_string("contact/emails/contact_admin.html", ctx)

    msg = EmailMultiAlternatives(
        subject=f"Заявка с сайта: {obj.subject}",
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.CONTACT_TO_EMAIL],
        reply_to=[obj.email] if obj.email else None,
    )
    msg.attach_alternative(html_body, "text/html")
    msg.send(fail_silently=False)

    # ===== ОТКУДА ПРИШЛА ФОРМА =====
    source = request.POST.get("form_source")

    # ===== ФУТЕР =====
    if source == "footer":
        return render(
            request,
            "contact/partials/footer_success.html",
            {
                "message": "Сообщение отправлено! Мы скоро свяжемся с вами.",
            }
        )

    # ===== СТРАНИЦА КОНТАКТОВ =====
    return render(
        request,
        "contact/partials/contact_success.html",
        {
            "message": "Сообщение отправлено! Мы скоро свяжемся с вами.",
            "form": ContactFormForm(),  # новая пустая форма
            "contact_info": contact_info,
        }
    )
