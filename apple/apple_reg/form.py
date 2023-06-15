from django.forms import ModelForm
from .models import Apple


class CreateAppleForm(ModelForm):
    class Meta(ModelForm):
        model = Apple
        fields = (
            'year_of_production',
            'breed',
            'row',
            'column',
           'geolocation',
        )

