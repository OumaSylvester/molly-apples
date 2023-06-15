from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in ['password1', 'password2']:
            self.fields[field].help_text = None

    class Meta(UserCreationForm):
            model = CustomUser
            fields = (
                'first_name',
                'last_name',
                'email',
                'id_number',
            )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'id'
        )
