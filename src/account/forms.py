from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser
from common.django_utils import AsyncFormMixin, AsyncModelFormMixin

class CustomUserCreationForm(UserCreationForm, AsyncFormMixin):

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'is_writer',
        )
    #:
#:

async def ais_valid(self):
    pass