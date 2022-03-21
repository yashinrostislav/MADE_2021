class Point:

    def __init__(self, coordinate_1, coordinate_2):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2


class Vector:

    def __init__(self, point_1, point_2):
        self.vect_c_1 = point_2.coordinate_1 - point_1.coordinate_1
        self.vect_c_2 = point_2.coordinate_2 - point_1.coordinate_2

    def vector_multiplication(self, other):
        return self.vect_c_1 * other.vect_c_2 - self.vect_c_2 * other.vect_c_1

    def scalar_multiplication(self, other):
        return self.vect_c_1 * other.vect_c_1 + self.vect_c_2 * other.vect_c_2


def in_segment(pnt1, pnt2, pnt3):
    am = Vector(pnt2, pnt1)
    bm = Vector(pnt3, pnt1)
    if (am.vector_multiplication(bm) == 0) and (am.scalar_multiplication(bm) <= 0):
        print('YES')
    else:
        print('NO')


def main():
    p1x, p1y, p2x, p2y, p3x, p3y = map(int, input().split())
    pnt1 = Point(p1x, p1y)
    pnt2 = Point(p2x, p2y)
    pnt3 = Point(p3x, p3y)
    in_segment(pnt1, pnt2, pnt3)


if __name__ == '__main__':
    main()
