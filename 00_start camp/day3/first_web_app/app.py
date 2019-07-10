from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')     # / 뒤에 오면 def 밑의 내용을 실행해라. 
def index():
    return render_template('index.html')


@app.route('/pick_lotto')     
def pick_lotto():
    numbers = range(1,46)
    lucky = random.sample(numbers, 6)
    return str(lucky)
    

# @app.route('/get_lotto/<int:num>')  #/<int:num> 뒤의 자리가 확정되어 있지는 않다. 
# def get_lotto_1():
#     #1회차 로또정보



@app.route('/pick_lunch/<int:count>')   #사용자 입력을 받는 방법 : var routing
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '사천탕수육',
        '마라탕'
    ]
    picks = random.sample(menus, count)
    return str(picks)         #스트링만 나갈 수 있다.  
    

@app.route('/cube/<int:count>')
def cube(count):
    return str(count ** 3)



if __name__ == '__main__':
    app.run(debug=True)






