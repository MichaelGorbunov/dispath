from django.forms import ModelForm, BooleanField
from .models import Mailing, Message, Recipient
class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class RecipientForm(StyleFormMixin,ModelForm):
    class Meta:
        model = Recipient
        fields = "__all__"
        exclude = ["ownership"]


class MessageForm(StyleFormMixin,ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class MailingForm(StyleFormMixin,ModelForm):
    class Meta:
        model = Mailing
        fields = "__all__"
        exclude = ["ownership", "enabled"]

    def __init__(self, *args, **kwargs):
        # Извлекаем текущего пользователя из переданных параметров
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['recipients'].queryset = Recipient.objects.filter(ownership_id=user.id)
            # фильтрация получателей по текущему пользователю



class ModeratorMailingForm(StyleFormMixin,ModelForm):
    class Meta:
        model = Mailing
        fields = "__all__"
        # exclude = ["ownership"]
