# 파일명을 변경하지 마시오.
# 아래에 Word 클래스를 작성하시오.


class Word():
    
    # 인스턴스 생성할 떄 빈 딕셔너리 
    def __init__(self):
        wordbook = {}

    # 영문과 한글 인자를 받을 때 wordbook에 넣기 
    def add(self, e, k):
        wordbook[e] = k
    
    
    def delete(self, en):
        # 만약 wordbook의 키값들 중에 en 이 있다면
        if en in wordbook.keys():
            # 그 en 를 wordbook에서 제거하고
            wordbook.remove(en)
            # return 
            return True
        # 만약 en 이 wordbook에 없으면 return False
        else:
            return False

    def print(self):
        return wordbook

# wordbook 이 정의 되지 않았다고 자꾸 에러가 떴어요... ㅠㅠㅠ 


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
