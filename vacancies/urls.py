from django.urls import path
from . import views

app_name = "vacancies"

urlpatterns = [
    path("", views.vacancy_list, name="list"),
    path("export/xlsx/", views.export_applications_xlsx, name="export_xlsx"),
    path("<slug:slug>/", views.vacancy_detail, name="detail"),
    path("<slug:slug>/apply/", views.vacancy_apply, name="apply"),
]