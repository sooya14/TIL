from django.shortcuts import render, HttpResponse, redirect
from art import *
import datetime, time


def index(request):
    return render(request, 'utils/index.html')

def art(request):
    fonts = ['chunky', 'caligraphy', 'bear', 'alpha',]
    return render(request, 'utils/art.html', {
        'fonts': fonts, 
    })

# def output(request):
#     user_input = request.GET.get('user-input')  # GET 방식으로 날라오면 딕셔너리에서 꺼내겠다.
#     user_font = request.GET.get('user-font')

#     if not user_input:
#         user_input = 'NONONO'
        
#     result = text2art(user_input, font=user_font)

#     return render(request, 'utils/output.html', {
#             'result': result,
#     })
   
def output(request):
    user_input = request.GET.get('user-input')  # GET 방식으로 날라오면 딕셔너리에서 꺼내겠다.
    user_font = request.GET.get('user-font')

    if user_input:
        result = text2art(user_input, font=user_font)
        return render(request, 'utils/output.html', {
            'result': result,
        })
    else:
        return redirect('/utils/art/')  # 아무것도 안넣었을 때 다시 '/utils/art/' 로 돌아가도록 


schs = {
        '월말평가 1': {'date': '2019-08-02', 'content': '월말평가 (파이썬)', 'text': '끝났다!!',},
        '회식': {'date': '2019-08-12', 'content': '두번째 회식', 'text': '불월',},
        '과목평가 1': {'date': '2019-08-23', 'content': '과목평가 (알고리즘)', 'text': '알고리즘......ㅠㅠㅠㅠ',}, 
        '월말평가 2': {'date': '2019-08-30', 'content': '월말평가 (알고리즘)','text': '화이팅...☆',},
    }

def throw(request):

    return render(request, 'utils/throw.html', {
        'schs': schs,
    })


def catch(request):
    user_input = request.GET.get('user-input')
    date = schs[user_input]['date']
    content = schs[user_input]['content']
    text = schs[user_input]['text']

    return render(request, 'utils/catch.html', {
        'user_input': user_input, 'date': date, 'content': content, 'text': text,})
   
  