from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', ]  # добавьте необходимые поля

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PasswordResetRequestForm(forms.Form):
    """Форма запрашивает у пользователя email для восстановления пароля"""
    email = forms.EmailField(label="Введите ваш email")


class SetNewPasswordForm(forms.Form):
    """Форма для ввода нового пароля"""
    new_password = forms.CharField(widget=forms.PasswordInput, label="Новый пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают.")


class CustomUserBlockUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # fields = "__all__"
        fields = ['username', 'is_active']

        def __init__(self, *args, **kwargs):
            super(CustomUserBlockUpdateForm, self).__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].help_text = ""
