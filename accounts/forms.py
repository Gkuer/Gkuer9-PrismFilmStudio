from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomAuthenticationFrom(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        
class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)