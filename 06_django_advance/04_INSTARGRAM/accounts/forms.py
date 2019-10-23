from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm  # 가입, 수정, 로그인 

from django.contrib.auth import get_user_model  # from .models import User 같은 것 / 하나만 바꿔도 나머지 다 저절로 바뀌기 때문에 사용한다. 
User = get_user_model() 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


# 예외로 돌아가는게 많은 코드... 
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:  # 로그인이 목적인 애여서 Meta 에서 상속받지 않아도 된다. 
        model = User