from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
import os

from openpyxl import Workbook

from .models import Vacancy, VacancyApplication
from .forms import VacancyApplicationForm


def vacancy_list(request):
    вакансии = Vacancy.objects.filter(is_active=True)
    return render(request, "vacancies/vacancy_list.html", {"vacancies": вакансии})


def vacancy_detail(request, slug):
    vacancy = get_object_or_404(Vacancy, slug=slug, is_active=True)
    form = VacancyApplicationForm()
    return render(request, "vacancies/vacancy_detail.html", {"vacancy": vacancy, "form": form})


def vacancy_apply(request, slug):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed")

    vacancy = get_object_or_404(Vacancy, slug=slug, is_active=True)
    form = VacancyApplicationForm(request.POST, request.FILES)

    if not form.is_valid():
        return render(request, "vacancies/partials/apply_form.html", {"vacancy": vacancy, "form": form})

    app = form.save(commit=False)
    app.vacancy = vacancy
    app.save()

    created_at = timezone.localtime(app.created_at).strftime("%d.%m.%Y %H:%M")

    subject = f"Отклик на вакансию: {vacancy.title}"
    text_body = (
        f"Вакансия: {vacancy.title}\n"
        f"ФИО: {app.full_name}\n"
        f"Телефон: {app.phone}\n"
        f"Email: {app.email}\n"
        f"Дата: {created_at}\n\n"
        f"Сопроводительное письмо:\n{app.cover_letter or '-'}\n"
    )

    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=getattr(settings, "HR_TO_EMAIL", []) or ["HR@tess-project.kz"],
        reply_to=[app.email],
    )

    # вложение резюме
    if app.resume:
        app.resume.open("rb")
        msg.attach(app.resume.name.split("/")[-1], app.resume.read(), "application/octet-stream")
        app.resume.close()

    msg.send(fail_silently=False)

    ctx2 = {
        "full_name": app.full_name,
        "vacancy_title": vacancy.title,
        "created_at": created_at,
        "email": app.email,
        "phone": app.phone,
        "cover_letter": app.cover_letter,
        "resume_filename": app.resume.name.split("/")[-1] if app.resume else "",
        # так же как в contact-шаблоне (там условие if site_url)
        "site_url": "https://tess-project.kz",
    }

    text_body2 = render_to_string("vacancies/emails/application_client.txt", ctx2)
    html_body2 = render_to_string("vacancies/emails/application_client.html", ctx2)

    reply = EmailMultiAlternatives(
        subject=f"Мы получили ваше резюме — {vacancy.title}",
        body=text_body2,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[app.email],
        reply_to=["HR@tess-project.kz"],
    )
    reply.attach_alternative(html_body2, "text/html")

    # CID logo — 1:1 как в contact
    logo_path = os.path.join(settings.MEDIA_ROOT, "about", "logo.png")
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            img = MIMEImage(f.read())
            img.add_header("Content-ID", "<tess_logo>")
            img.add_header("Content-Disposition", "inline", filename="logo.png")
            reply.attach(img)

    reply.send(fail_silently=False)

    return render(
        request,
        "vacancies/partials/apply_success.html",
        {"vacancy": vacancy, "message": "Отклик отправлен! Мы свяжемся с вами при необходимости."},
    )


@staff_member_required
def export_applications_xlsx(request):
    """
    Выгрузка всех откликов в Excel (кнопка в админке или отдельная ссылка).
    """
    wb = Workbook()
    ws = wb.active
    ws.title = "Applications"

    ws.append(["Дата", "Вакансия", "ФИО", "Телефон", "Email", "Сопроводительное", "Файл резюме", "Обработано"])

    qs = VacancyApplication.objects.select_related("vacancy").order_by("-created_at")
    for a in qs:
        ws.append([
            timezone.localtime(a.created_at).strftime("%d.%m.%Y %H:%M"),
            a.vacancy.title,
            a.full_name,
            a.phone,
            a.email,
            (a.cover_letter or "").strip(),
            a.resume.name if a.resume else "",
            "Да" if a.is_processed else "Нет",
        ])

    resp = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    resp["Content-Disposition"] = 'attachment; filename="vacancy_applications.xlsx"'
    wb.save(resp)
    return resp