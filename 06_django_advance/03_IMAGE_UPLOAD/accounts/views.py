from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm


@require_http_methods(['GET', 'POST'])
def signup(request):  # new user

    # 사용자가 회원가입할 데이터를 보냈다는 뜻 
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  # 사용자가 데이터를 넣어 놓은 시험지 
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


def login(request):
    pass

def logout(request):
    pass
