from django.urls import path
from.views import CreateAppleView

urlpatterns = [
    path('register-apple', CreateAppleView.as_view(), name='apple_register'),
]

