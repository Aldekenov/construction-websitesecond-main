from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column
from .models import ContactForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'phone', 'contact_type', 'subject', 'message']
        labels = {
            "name": _("Имя"),
            "email": _("Email"),
            "phone": _("Телефон"),
            "contact_type": _("Тип обращения"),
            "subject": _("Тема"),
            "message": _("Сообщение"),
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.attrs = {
            'hx-post': reverse_lazy('contact:contact_submit'),
            'hx-target': '#contact-form-container',
            'hx-swap': 'innerHTML'
        }

        self.helper.layout = Layout(
            Row(
                Column('name', css_class='w-full md:w-1/2 px-2'),
                Column('email', css_class='w-full md:w-1/2 px-2'),
                css_class='flex flex-wrap -mx-2'
            ),
            Row(
                Column('phone', css_class='w-full md:w-1/2 px-2'),
                Column('contact_type', css_class='w-full md:w-1/2 px-2'),
                css_class='flex flex-wrap -mx-2'
            ),
            Field('subject'),
            Field('message'),
            Submit('submit', _('Отправить'),
                   css_class='bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded')
        )

        # Add Tailwind classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            })