from django.shortcuts import render, redirect, get_object_or_404

# accounts 에서 import 할 모든 함수들은 django.contrib.auth
from django.contrib.auth import login as auth_login, logout as auth_logout  # 걍 공식으로 암기 ㅎㅎ

# User 모델을 가져오는 함수 
from django.contrib.auth import get_user_model

# accounts 에서 import 할 Form(UCF, AF)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # 잘 모르겟으면 들어가서 찾기 
# decorator
from django.contrib.auth.decorators import login_required



# 중요! 
# @require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:  # is_authenticated 는 함수가 아니다!!! / 로그인을 했다면 
        return redirect('articles:article_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 그냥 습관적으로 하자잇
            # login 을 하도록 합시다! 인자가 2개다 
            auth_login(request, user)  # 오픈북 
            return redirect('articles:article_list')  # 그냥 url 만 던지면 된다. 단순히 보내는 것 
    else: 
        form = UserCreationForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })  # 인자가 많은 것은 얘
    


# 위에꺼 복사해오기 => 1. form 바꿔끼기 2. save 가 아니라 get_user
def login(request):
    if request.user.is_authenticated:  # is_authenticated 는 함수가 아니다!!! / 로그인을 했다면 
        return redirect('articles:article_list')

    if request.method == 'POST':
        # 1. AuthForm 은 인자가 2개(request, request.POST) => 얘만 유일하게 인자가 2개!!!!! 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 성공 => 성공한 user 을 꺼낸다. 
            user = form.get_user() 
            # login 을 하도록 합시다! 인자가 2개다 
            auth_login(request, user)  
            # 나는 못해요... 
            return redirect('articles:article_list')
            # 나는 할 수 있어요! 
            # return redirect(request.GET.get('next') or 'articles:article_list')  # 그냥 url 만 던지면 된다. 단순히 보내는 것 
    else: 
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })  
    

def logout(request):
    # auth_logout 은 인자가 1개 => 잘 모르겟으면 오픈북 
    auth_logout(request)
    return redirect('articles:article_list')



