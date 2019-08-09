# 파일명을 변경하지 마시오.
# 아래에 Word 클래스를 작성하시오.

class Word:
    
    def __init__(self):
        self.wordbook = {} 

    def add(self, eng, kor):  # wb.add('grape', '포도')
        self.wordbook[eng] = kor
        self.wordbook  # {'grape': '포도'}
        # self.wordbook.update(eng=kor) => {eng: '포도'} 사용하지 않는 것이 조으다. 

    def delete(self, key):
        if key in self.wordbook:
            self.wordbook.pop(key)
            return True
        else:
            return False

    # class 안에 들어있기 때문에 글로벌의 프린트와 상관이 없다. 기존의 print() 와 덮어쓰지 않는다.
    def print(self):
        for key, value in self.wordbook.items():
            print(f'{key}: {value}')



# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    my_book = Word()
    my_book.add('grape', '포도')
    my_book.add('peach', '복숭아')
    my_book.add('watermelon', '수박')
    my_book.add('mango', '망고')
    my_book.print()
    print(my_book.delete('watermelon'))
    print(my_book.delete('mango'))
    print(my_book.delete('carrot'))
    my_book.print()
