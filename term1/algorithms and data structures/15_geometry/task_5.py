class Point:

    def __init__(self, coordinate_1, coordinate_2):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2


class Vector:

    def __init__(self, point_1, point_2):
        self.vect_c_1 = point_2.coordinate_1 - point_1.coordinate_1
        self.vect_c_2 = point_2.coordinate_2 - point_1.coordinate_2


def vector_multiplication(vector_1, vector_2):
    return vector_1.vect_c_1 * vector_2.vect_c_2 - vector_1.vect_c_2 * vector_2.vect_c_1


def distance(point_1, point_2):
    return (point_1.coordinate_1 - point_2.coordinate_1) ** 2 + (point_1.coordinate_2 - point_2.coordinate_2) ** 2


def get_convex_hull(points_list):
    convex_hull = []
    points_list = sorted(points_list)

    return convex_hull


def find_perimetr(convex_hull):
    perimetr = 0
    for (point_1, point_2) in convex_hull:
        perimetr += distance(point_1, point_2)
    return perimetr


def main():
    n = int(input())
    points_list = []
    for _ in range(n):
        pt1, pt2 = map(int, input().split())
        pnt = Point(pt1, pt2)
        points_list.append(pnt)
        print(f"x: {pnt.coordinate_1}, y: {pnt.coordinate_2}")


if __name__ == '__main__':
    main()

