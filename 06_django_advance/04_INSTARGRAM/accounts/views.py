from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth import login as auth_login, logout as auth_logout

# 회원가입용 Form, 인증(로그인)용 Form
from .forms import CustomAuthenticationForm, CustomUserCreationForm
# 현재 Project 에서 사용할 User 모델을 return 하는 함수 
from django.contrib.auth import get_user_model  # 알아서 settings 의 user model 자체를 가져온다. 
User = get_user_model()  # 


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')

    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')

    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('/')


@require_GET # GET 요청으로 화면만 넘겨준다. 
def user_page(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/user_page.html', {
        'user_info': user_info,  # user 라고 하면 덮어씌워진다. 
    })




def follow(request, user_id):
    fan = request.user # 요청을 보낸 사용자
    star = get_object_or_404(User, id=user_id)

    if fan != star:  # 내가 나를 팔로워할 수 없게 
        if star.fans.filter(id=fan.id).exists():
            star.fans.remove(fan)
        else:
            star.fans.add(fan)
    return redirect(star)  # 내가 팔로우한 사람의 개인 페이지로 간다. 


 



