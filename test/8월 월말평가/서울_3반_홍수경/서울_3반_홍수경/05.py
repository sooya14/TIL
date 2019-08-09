# 파일명을 변경하지 마시오.
# 아래에 Point 클래스 및 Rectangle 클래스를 작성하시오.


class Point():
    
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Rectangle():
    
    def __init__(self, p1, p2):
        self.p1 = p1.x, p1.y
        self.p2 = p2.x, p2.y

    # x좌표의 차와 y좌표의 차를 통해서 계산
    def get_area(self):
        if p1.x < p2.x:
            a = p2.x - p1.x
        else:
            a = p1.x - p2.x
        if p1.y < p2.y:
            b = p2.y - p1.y
        else:
            b = p1.y - p2.y 
        return a * b

    def get_perimeter(self):
        if p1.x < p2.x:
            a = p2.x - p1.x
        else:
            a = p1.x - p2.x
        if p1.y < p2.y:
            b = p2.y - p1.y
        else:
            b = p1.y - p2.y 
        return a * 2 + b * 2

    # x 좌표의 차이와 y 좌표의 차이가 같으면 정사각형, 아니면 직사각형
    def is_square(self):
        if p1.x < p2.x:
            a = p2.x - p1.x
        else:
            a = p1.x - p2.x
        if p1.y < p2.y:
            b = p2.y - p1.y
        else:
            b = p1.y - p2.y 
        if a == b :
            return True
        else:
            return False
    

# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    p1 = Point(1, 3)
    p2 = Point(3, 1)
    r1 = Rectangle(p1, p2)
    print(r1.get_area())
    print(r1.get_perimeter())
    print(r1.is_square())
    p3 = Point(3, 7)
    p4 = Point(6, 4)
    r2 = Rectangle(p3, p4)
    print(r2.get_area())
    print(r2.get_perimeter())
    print(r2.is_square())