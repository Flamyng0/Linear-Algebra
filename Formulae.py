import numpy as np
import math


input_num = int(input("""1 : Distance b/w 2 Vectors Calculator 
2 : (proj)Projection of 2 on 1 
3 : (perp)The vector projection of 2 perpendicular to 1 
4 : Area of parallelogram 
5 : Area of Triangle """))

if input_num == 1:
    vector_1 = [int(input("Vector 1: ")) for i in range(3)]
    vector_2 = [int(input("Vector 2: ")) for i in range(3)]

    distance = math.sqrt(vector_2[0] - vector_1[0] + vector_2[1] - vector_1[1] + vector_2[2] - vector_1[2])

    print("Distance: ", distance)

if input_num == 2:
    vector_1 = [int(input("Vector 1: ")) for i in range(3)]
    vector_2 = [int(input("Vector 2: ")) for i in range(3)]

    proj_top = np.dot(vector_1, vector_2)
    proj_bottom = np.linalg.norm(vector_1) ** 2
    proj_final = np.multiply(vector_1, (proj_top / proj_bottom))

    print(proj_final)

if input_num == 3:
    vector_1 = [int(input("Vector 1: ")) for i in range(3)]
    vector_2 = [int(input("Vector 2: ")) for i in range(3)]

    proj_top = np.dot(vector_1, vector_2)
    proj_bottom = np.linalg.norm(vector_1) ** 2
    proj_final = np.multiply(vector_1, (proj_top / proj_bottom))

    perp = vector_2 - proj_final

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