import numpy as np
import math


input_num = int(input("""1 : Distance b/w 2 Vectors Calculator 
2 : (proj)Projection of 2 on 1 
3 : (perp)The vector projection of 2 perpendicular to 1 
4 : Area of parallelogram 
5 : Area of Triangle 
6 : A point which is minimum distance b/w point and plane 
7 : Minimum Distance b/w point and plane
8 : Intersection b/w two planes **
Insert Num ----- """))


def vector_sum(v1, v2):
    sum = []
    for i in range(len(v1)):
        sum.append(v1[i] + v2[i])
    return sum


def make_vector(p1, p2):
    vector = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
    return vector


def projection(v1, v2):
    proj_top = np.vdot(v1, v2)
    proj_bottom = np.linalg.norm(v1) ** 2
    proj_final = np.multiply(v1, (proj_top / proj_bottom))
    return proj_final


def calc_point(point_g, normal_n):
    point = (normal[0] * (point_g[0] + 1) + normal_n[1] * (point_g[1]) - normal_n[3]) / -normal_n[2]
    return point


if input_num == 1:
    vector_1 = [int(input("Vector 1: ")) for i in range(3)]
    vector_2 = [int(input("Vector 2: ")) for i in range(3)]

    distance = math.sqrt(vector_2[0] - vector_1[0] + vector_2[1] - vector_1[1] + vector_2[2] - vector_1[2])

    print("Distance: ", distance)

if input_num == 2:
    vector_1 = [int(input("Vector 1: ")) for i in range(3)]
    vector_2 = [int(input("Vector 2: ")) for i in range(3)]

    proj = projection(vector_1, vector_2)

    print(proj)

if input_num == 3:
    vector_1 = [int(input("Vector 1: ")) for i in range(3)]
    vector_2 = [int(input("Vector 2: ")) for i in range(3)]

    proj = projection(vector_1, vector_2)
    perp = vector_2 - proj

    print(perp)


if input_num == 4:
    n = int(input("\nInput the number of dimensions: "))
    vector_1 = [int(input("Vector 1: ")) for i in range(n)]
    vector_2 = [int(input("Vector 2: ")) for i in range(n)]

    dot = np.dot(vector_1, vector_2) ** 2
    v1 = np.linalg.norm(vector_1) ** 2
    v2 = np.linalg.norm(vector_2) ** 2

    area = math.sqrt(v1 * v2 - dot)

    print(area)

if input_num == 5:
    vector_1 = [int(input("Vector 1: ")) for i in range(3)]
    vector_2 = [int(input("Vector 2: ")) for i in range(3)]

    dot = np.dot(vector_1, vector_2) ** 2
    v1 = np.linalg.norm(vector_1) ** 2
    v2 = np.linalg.norm(vector_2) ** 2

    area = math.sqrt(v1 * v2 - dot) * 0.5

    print(area)

if input_num == 6:
    point_1 = [int(input("Point 1: ")) for i in range(3)]
    normal = [int(input("Plane (insert only the coefficients A, B, C, and D): ")) for i in range(4)]

    point_2 = [(point_1[0] + 1), point_1[1], calc_point(point_1, normal)]
    vector_1 = make_vector(point_1, point_2)
    n = normal[:3]
    proj_point = projection(vector_1, n)
    final_point = vector_sum(proj_point, point_1)

    print(final_point)


if input_num == 7:
    point = [int(input("Point 1: ")) for i in range(3)]
    normal = [int(input("Plane (insert only the coefficients A, B, C, and D): ")) for i in range(4)]

    distance_bottom = np.linalg.norm(normal[:3])
    distance_top = abs(normal[0] * point[0] + normal[1] * point[1] + normal[2] * point[2] + normal[3])
    distance = distance_top / distance_bottom

    print(distance)

