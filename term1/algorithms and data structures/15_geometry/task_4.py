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


def main():
    ans = 0
    polygon = []
    n = int(input())
    for _ in range(n):
        px, py = (map(int, input().split()))
        polygon.append(Point(px, py))

    for i in range(1, n):
        radius1 = Vector(polygon[0], polygon[i])
        radius2 = Vector(polygon[0], polygon[(i + 1) % n])
        ans += radius1.vector_multiplication(radius2)

    print(abs(ans) / 2)


if __name__ == '__main__':
    main()
