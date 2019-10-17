from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 

from django.contrib.auth import login as auth_login, logout as auth_logout
# 알아서 로그인 해주는 함수 / 이름이 겹치니깐 다르게 부르겠다 (그렇게 안하면 함수에서 재귀함수가 되어버린다. )  


@require_http_methods(['GET', 'POST'])
def signup(request):  # new user
    if request.user.is_authenticated: # 로그인 했으면 signup 못하게 만들기 위해 막아버리기 
        return redirect('sns:posting_list')

    # 사용자가 회원가입할 데이터를 보냈다는 뜻 
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  # 사용자가 데이터를 넣어 놓은 시험지 / 회원가입하는 form 
        if form.is_valid():  # 채점 
            user = form.save()
            return redirect('sns:posting_list')
        # else:
        #     return render(request, 'accounts/signup.html', {
        #         'form': form,  # 실패된 form 이다. / 망한 시험지 
        #     })
    
    else:  # 사용자가 회원가입 HTML 을 달라는 뜻 
        form = UserCreationForm()  # 시험지 인데 아직 답을 입력하지 않은 셤이다. 새시험지 

    return render(request, 'accounts/signup.html', {
        'form': form,   # 새로운 시험지가 나온다. 
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated: # 사용자가 로그인한 상태라면, 무시
        return redirect('sns:posting_list')  

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)  # 사용자 인증하는 form / 이 form 만 데이터 받아오는 방식이 좀 다르다. 
        if form.is_valid():

            # 쿠키와 세션을 한꺼번에 세팅해준다. 
            auth_login(request, form.get_user())  # form.get_user : form 검증을 통과한 사용자를 꺼내오겠다. == user 
            return redirect('sns:posting_list')  

            # 쿠키세팅
            # response = redirect('sns:posting_list')
            # response.set_cookie(key='nickname', value='idot', max_age=5)  # return 이 없다. 원본을 바꿀수 있다. # 쿠키세팅 => 닉네임을 설정했고 5초가 지나면 사라진다. 
            # return response
            
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('sns:posting_list')
