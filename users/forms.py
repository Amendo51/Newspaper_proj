from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomeUserCreationForm(UserCreationForm):
    class meta(UserCreationForm.meta):
        model = CustomUser
        field = UserCreationForm.Meta.fields + ('age',)
class CustomUserChangeForm(UserChangeForm):

    class Meta:
            model = CustomUser
            fields = UserChangeForm.fields