# 파일명을 변경하지 마시오.
# 아래에 Point 클래스 및 Rectangle 클래스를 작성하시오.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2
        # 굳이 반복하지 않고 생성자에 넣어서 할 수도 있다. 
        # self.garo = abs(self.p2.x - self.p1.x)
        # self.sero = abs(self.p1.y - self.p2.y)

    def get_area(self):
        garo = abs(self.p2.x - self.p1.x)
        sero = abs(self.p1.y - self.p2.y)
        return garo * sero
        # return self.garo * self.sero

    def get_perimeter(self):
        garo = abs(self.p2.x - self.p1.x)
        sero = abs(self.p1.y - self.p2.y)
        return (garo+sero) * 2

    def is_square(self):
        garo = abs(self.p2.x - self.p1.x)
        sero = abs(self.p1.y - self.p2.y)
        return garo == sero



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
