from django.shortcuts import render, HttpResponse
import json

# Create your views here.
def index(request):
    return HttpResponse('Hi django :)')

def about(request):
    me = {
        'name': '수경', 
        'role': 'ssafy', 
        'email': 'soo14906@naver.com',
    }

    return HttpResponse(json.dumps(me))

# HTML 을 내보내고 싶다. 
def portfolio(request):
    return render(request, 'portfolio.html')  # render : html 을 내보내는 함수 
    # request(무조건 기입), 'porfolio.html' (사용하고 싶은 파일명)


# /pages/help/ => help() view 함수 실행 => help.html (내용무관)
def help(request):
    return render(request, 'help.html')

