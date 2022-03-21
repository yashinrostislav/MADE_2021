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
    return (am.vector_multiplication(bm) == 0) and (am.scalar_multiplication(bm) <= 0)


def intersecting_segments(pnt1, pnt2, pnt3, pnt4):
    p1p2 = Vector(pnt1, pnt2)
    p1m1 = Vector(pnt1, pnt3)
    p1m2 = Vector(pnt1, pnt4)
    m1m2 = Vector(pnt3, pnt4)
    m1p2 = Vector(pnt3, pnt2)
    m1p1 = Vector(pnt3, pnt1)

    return (p1p2.vector_multiplication(p1m1) * p1p2.vector_multiplication(p1m2) < 0
            and (m1m2.vector_multiplication(m1p1) * m1m2.vector_multiplication(m1p2) < 0))\
           or (in_segment(pnt3, pnt1, pnt2) or in_segment(pnt4, pnt1, pnt2) or
               in_segment(pnt1, pnt3, pnt4) or in_segment(pnt2, pnt3, pnt4))


def main():
    ans = 0
    DEFAULT_X = -(10 ** 7) + 131
    DEFAULT_Y = -(10 ** 7) + 213
    point_away = Point(DEFAULT_X, DEFAULT_Y)
    polygon = []
    n, p1x, p1y = map(int, input().split())
    req_point = Point(p1x, p1y)
    for _ in range(n):
        px, py = (map(int, input().split()))
        polygon.append(Point(px, py))

    for i in range(n):
        if in_segment(req_point, polygon[i % n], polygon[(i + 1) % n]):
            print('YES')
            exit()

    for i in range(n):
        if intersecting_segments(req_point, point_away, polygon[i % n], polygon[(i + 1) % n]):
            ans += 1

    if ans % 2 == 1:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
