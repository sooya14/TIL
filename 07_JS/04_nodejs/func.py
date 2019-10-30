# REPL === Read Evalute Print Loop

# > ((x, y) => { return x + y; })(1, 2)
# 3
# > [1, 2, 3][0]
# 1
# 함수는 객체이기 때문에 가능하다. => 이름 설정하지 않고서 가능

def add(x, y):
    return x + y

calculator = {
    'add': lambda x, y: x + y
}
print (calculator['add'](1, 2))

# 1급 객체 : int string arr/list obj/dict FUNCTION
# 인자로 넘어갈 수 있고, return 으로 나올 수 있다. 
def a():
    def add(x, y):
        return x + y

    return add

print(a()(1, 2))


from . import views

path('asdf/', views.index)
addEventListener('click', function() {
    console.log('클릭')
})  # => 콜백함수

def index(request):
    return HttpResponse


# map 함수는 첫번째 인자로 함수를 받아야한다. 
new_map = map(str, [1, 2, 3])
yy = list(new_map)

def map2(cb, iter):
    result = []
    for x in iter:
        result.append(str(x))
    return result

xx = map2(str, [1, 2, 3])

