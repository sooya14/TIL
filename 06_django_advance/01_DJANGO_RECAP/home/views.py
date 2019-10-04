from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'home/index.html')

def guess(request):  # request 아니여도 된다ㅇㅅㅇ 
    return render(request, 'home/guess.html') # 앞이 이름 설정하는 부분 
    
def answer(request):
    # 채점 
    # 대괄호 안쓰는 이유는? 있든 없든 진행을 시키키 위해 

    cnt = 0
    if request.GET.get('q1') == '940906':
        cnt += 1
    if request.GET.get('q2') == '롯데':
        cnt += 1
    if request.GET.get('q3') == 'A':
        cnt += 1
    
    return render(request, 'home/answer.html', {'cnt': cnt})