from django import forms
from .models import VacancyApplication


class VacancyApplicationForm(forms.ModelForm):
    class Meta:
        model = VacancyApplication
        fields = ["full_name", "phone", "email", "cover_letter", "resume"]
        widgets = {
            "cover_letter": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_resume(self):
        f = self.cleaned_data["resume"]
        allowed = {
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        }
        if hasattr(f, "content_type") and f.content_type not in allowed:
            raise forms.ValidationError("Разрешены только PDF/DOC/DOCX.")
        if f.size > 10 * 1024 * 1024:
            raise forms.ValidationError("Файл слишком большой (макс 10 МБ).")
        return f