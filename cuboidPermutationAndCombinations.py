from itertools import permutations

import numpy as np
import itertools


# def generate_cuboid_coordinates(x,y,z):
#     coordinates = []
#     for i in range(x + 1):
#         for j in range(y + 1):
#             for k in range(z + 1):
#                 coordinates.append((i,j,k))
#     return coordinates
#
# def get_permutations(i, j, k):
#      return list(itertools.combinations(generate_cuboid_coordinates(i,j,k), 2))
# print(get_permutations(1, 2, 3))



# def arrayElements(arr):
#     if len(arr) > 0:
#         for i in range(len(arr)):
#             for j in range(len(arr[i])):
#                 print(arr[i][j])
#
# matrix = np.random.randint(10, size=(3,3))
# print('matrix =', matrix)
# arrayElements(matrix)

if __name__ == '__main__':
    x = int(input('Enter X:'))
    y = int(input('Enter Y:'))
    z = int(input('Enter Z:'))
    n = int(input('Enter N:'))

    coordinates = []
    iArray =[]
    jArray = []
    kArray = []

    for x in range(0, x + 1):
        iArray.append(x)
    for y in range(0, y + 1):
        jArray.append(x)
    for x in range(0, z + 1):
        kArray.append(x)
    for i in range(len(iArray)):
        for j in range(len(jArray)):
            for k in range(len(kArray)):
                if i+j+k != n:
                    coordinates.append([i,j,k])

    print(coordinates)


