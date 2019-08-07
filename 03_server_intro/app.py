# View 는 최고 중간관리자. 
from flask import Flask, render_template

app = Flask(__name__)

# 요청이 들어왔는데 url 에 / 로 끝나고 도메인 뒤에 아무말이 없으면. 
@app.route('/')  # 이렇게 요청이 들어오면, (무슨일이 일어나면) => 요청 request
def index():
    return render_template('index.html')  # 이 일을 해! => 응답 response

@app.route('/cube/<int:number>')  
def cube(number):
    return f'{number} 의 3제곱은 {number** 3} 입니다.'

# Workshop 08
@app.route('/dict/<string:word>')
def my_dict(word):
    d = {
        'apple': '사과', 
        'banana': '바나나',
    }

    result = d.get(word)
    if result:
        return f'{word}은(는) {d[word]}!'
    else:
        return f'{word}은(는) 나만의 단어장에 없는 단어입니다!'

    # if word in d:
    #     return f'{word}은(는) {d[word]}!'
    # else:
    #     return f'{word}은(는) 나만의 단어장에 없는 단어입니다!'


if __name__ == '__main__':
    app.run(debug=True)